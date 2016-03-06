__author__ = "Shiven"

import json
import urllib2

url = raw_input("Enter location: ")
print "Retrieving: ", url
if len(url) < 1:
    print "Please enter a valid url"
else:
    data = urllib2.urlopen(url).read()
    json_data = json.loads(data)
    comments = json_data['comments']
    total_comment_count = 0
    for comment in comments:
        total_comment_count += int(comment['count'])
    print total_comment_count
