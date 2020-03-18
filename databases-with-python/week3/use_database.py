import xml.etree.ElementTree as ET
import sqlite3

# 连接数据库
connect = sqlite3.connect('itunesdb.sqlite')
cur = connect.cursor()

# 创建表
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER, 
    genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER
);
''')

file_name = 'Library.xml'


# 查找是否有内容
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


# 获取所有的内容
stuff = ET.parse(file_name)
all_track = stuff.findall('dict/dict/dict')
print('Dict count:', len(all_track))

# 循环处理拿到的内容
for entry in all_track:
    if lookup(entry, 'Track ID') is None:
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, genre, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist,))
    artist_id = cur.execute('''SELECT id FROM Artist WHERE name = (?)''', (artist,)).fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre,))
    genre_id = cur.execute('''SELECT id FROM Genre WHERE name = (?)''', (genre,)).fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
    album_id = cur.execute('''SELECT id FROM Album WHERE title = (?)''', (album,)).fetchone()[0]

    cur.execute(
        '''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, genre_id, length, rating, count))

    connect.commit()
