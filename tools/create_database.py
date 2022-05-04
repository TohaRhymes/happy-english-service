import sqlite3
import sys


def create_db(path: str):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE subtitles
                    (video_id integer, duratuon integer, start_time integer, content text)''')

    cursor.execute('''CREATE TABLE videos
                    (video_id integer, link text)''')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    # python ./create_database.py ../database.sqlite
    path = sys.argv[1]
    create_db(path)
