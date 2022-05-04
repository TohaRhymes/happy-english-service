import sqlite3
import typing
from dataclasses import dataclass
import re


@dataclass
class VideoFragment:
    video_id: int
    duration: int
    start: int
    content: str


def search(phrase: str, path: str) -> typing.List[VideoFragment]:
    connection = sqlite3.connect(path)
    connection.create_function("REGEXP", 2, lambda expr, item: re.compile(expr).search(item.lower()) is not None)
    cursor = connection.cursor()

    rows = cursor.execute('''SELECT * FROM subtitles WHERE content REGEXP ? ;''',
                          (r'.*\W' + phrase.lower() + r'\W.*',))

    result = []
    for row in rows:
        data = VideoFragment(*row)
        print(data)
        video_id = data.video_id
        link = list(cursor.execute('''SELECT link FROM videos WHERE video_id=:id;''', {'id': video_id}))[0][0]
        start = int(data.start / 1000)
        duration = int(data.duration / 1000) + 1
        end = start + duration
        content = data.content
        result.append({'content': content,
                       'link': link})
        break
    connection.close()
    return result


if __name__ == '__main__':
    print(search('for the', '../database.sqlite'))
