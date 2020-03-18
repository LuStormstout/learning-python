# import sqlite3
#
# connect = sqlite3.connect('../../jacklucn.db')
# cur = connect.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER )')
#
# file_name = 'mbox-short.txt'
# file_handle = open(file_name)
# for line in file_handle:
#     if not line.startswith('From: '):
#         continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
#     connect.commit()
#
# sql_str = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sql_str):
#     print(str(row[0]), row[1])


import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = 'mobx.txt'
handle = open(file_name)
for line in handle:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

sql_str = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sql_str):
    print(str(row[0]), row[1])

cur.close()
