__author__ = "Shiven"

import urllib2
import xml.etree.ElementTree as ET

url = raw_input("Enter location: ")

if len(url) < 1:
    print "Please enter a valid url"
else:
    print "Retrieving: ", url
    xml = urllib2.urlopen(url).read()
    print xml
    tree = ET.fromstring(xml)
    comments = tree.findall('.//count')
    sum_comments = 0
    for comment in comments:
        sum_comments += int(comment.text)
    print sum_comments
