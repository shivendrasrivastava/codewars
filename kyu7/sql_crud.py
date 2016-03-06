__author__ = "Shiven"

import sqlite3
import urllib2
import re

conn = sqlite3.connect('emaildb.sqlite')

def get_data():
    url = raw_input("Enter location: ")
    data = urllib2.urlopen(url).read()
    filter_data(data)

def filter_data(data):
    email_from_list = re.findall(r'From \S+@(\S+)', data)
    email_map = dict()
    for email_domain in email_from_list:
        count = 0
        if not email_map.get(str(email_domain)):
            email_map[str(email_domain)] = 1
        else:
            count = email_map.get(str(email_domain))
            count += 1
            email_map[str(email_domain)] = count
    save_to_db(email_map)

def save_to_db(email_map):
    cur = connect_db()
    create_table(cur)
    #insert data into table now
    for key, value in email_map.items():
        print key, value
        cur.execute('''INSERT INTO COUNTS (org, count) VALUES (? , ?)''', (str(key), int(value)))
        commit_transaction()

def create_table(cur):
    cur.execute('''DROP TABLE IF EXISTS COUNTS''')
    cur.execute('''CREATE TABLE COUNTS (org TEXT, count INTEGER)''')

def connect_db():
    cur = conn.cursor()
    return cur

def commit_transaction():
    conn.commit()

if __name__ == "__main__":
    get_data()
