__author__ = "Shiven"

import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect("trackdb.sqlite")

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
    cur = conn.cursor()
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

if __name__ == "__main__":
    init()
