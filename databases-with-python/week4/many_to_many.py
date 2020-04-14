import json
import sqlite3

connect = sqlite3.connect('many_to_many.db')
cur = connect.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file_name = 'roster_data.json'
str_data = open(file_name).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    user_id = cur.execute('SELECT id FROM User WHERE name = ?', (name,)).fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    course_id = cur.execute('SELECT id FROM Course WHERE title = ?', (title,)).fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

    connect.commit()

res = cur.execute('''
SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
''').fetchone()
print(res)
