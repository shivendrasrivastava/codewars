__author__ = "Shiven"

import urllib2
from BeautifulSoup import *
import re

url = raw_input("Enter url - ")
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup("td")
number_list = []
for tag in tags:
    tag = str(tag)
    if bool(re.search(r'\d', tag)):
        number_list.append(int(re.findall(r'\d+', tag)[0]))
print sum(number_list)
