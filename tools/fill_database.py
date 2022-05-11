import json
import random
import re
import sqlite3
import sys
from time import sleep
from typing import List
from urllib.error import HTTPError
from urllib.request import urlopen
from tqdm import tqdm

SUBTITLES_URL = 'https://www.ted.com/talks/subtitles/id/{}/lang/en'
VIDEOS_URL = 'https://www.ted.com/talks/{}'


def download_subtitles(video_id: int) -> List[tuple]:
    url = SUBTITLES_URL.format(video_id)
    response = urlopen(url)
    data = response.read().decode('utf-8')
    captions = json.loads(data)['captions']
    return [(video_id, caption['duration'], caption['startTime'], caption['content']) for caption in captions]


def download_video_link(video_id: int) -> (int, str):
    url = VIDEOS_URL.format(video_id)
    response = urlopen(url)
    data = response.read().decode('utf-8')
    link = re.findall(r'https://py\.tedcdn\.com.*mp4', data)[0]
    return [video_id, link]


def fill_db(captions: List[tuple], link: (int, str), path: str) -> None:
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.executemany('''INSERT INTO subtitles VALUES (?, ?, ?, ?)''', captions)
    cursor.executemany('''INSERT INTO videos VALUES (?, ?)''', [link, ])
    connection.commit()
    connection.close()


if __name__ == '__main__':
    # python ./fill_database.py ../database.sqlite
    path = sys.argv[1]
    for i in tqdm(range(750, 100000)):
        try:
            captions = download_subtitles(i)
            link = download_video_link(i)
            fill_db(captions, link, path)
            sleep(3)
        except HTTPError:
            # if random.randint(1, 10) > 8:
            #     sleep(20)
            print('e')
            pass
