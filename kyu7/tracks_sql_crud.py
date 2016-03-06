__author__ = "Shiven"

import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

def init():
    create_table()
    tree = read_data_from_xml()
    parse_data(tree)

def read_data_from_xml():
    file_name = raw_input("Enter location: ")
    tree = ET.parse(file_name)
    print tree
    return tree

def create_table():
    cur.execute('''DROP TABLE IF EXISTS ARTIST''')
    cur.execute('''DROP TABLE IF EXISTS GENRE''')
    cur.execute('''DROP TABLE IF EXISTS ALBUM''')
    cur.execute('''DROP TABLE IF EXISTS TRACK''')
    print "Creating Table ARTIST"
    cur.execute('''CREATE TABLE ARTIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);''')
    print "Creating Table GENRE"
    cur.execute('''CREATE TABLE GENRE (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);''')
    print "Creating Table ALBUM"
    cur.execute('''CREATE TABLE ALBUM (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE);''')
    print "Creating Table TRACK"
    cur.execute('''CREATE TABLE TRACK (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER);''')
    conn.commit()

def parse_data(tree):
    data = tree.findall('dict/dict/dict')
    print "Complete data length: ",len(data)
    for entry in data:
        if (lookup(entry, 'Track ID') is None): continue
        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')
        genre = lookup(entry, "Genre")

        if name is None or album is None or artist is None:
            continue
        save_to_db(name, artist, album, count, rating, length, genre)

def save_to_db(name, artist, album, count, rating, length, genre):
    #Inserting data for Artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
    cur.execute('SELECT id FROM ARTIST WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    #Inserting data for Album
    print "Inserting Album ", album
    print "Inserting artist id", artist_id
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    #Inserting data into Genre
    print "Inserting Genre ", genre
    if not genre is None:
        cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
        genre_id = cur.fetchone()[0]
        print album, album_id, genre_id, length, rating, count
        cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (album, album_id, genre_id, length, rating, count))

    conn.commit()


def lookup(tag, key):
    found = False
    for child in tag:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

if __name__ == "__main__":
    init()
