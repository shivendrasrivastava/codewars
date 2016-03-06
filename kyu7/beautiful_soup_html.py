__author__ = "Shiven"
import re
import urllib2
from BeautifulSoup import *

url = raw_input("Enter the url :- ")
count = 1
while count <= 7:
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup("a")
    url = str(tags[17].get('href', None))
    count += 1
print url
