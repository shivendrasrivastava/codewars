__author__ = "Shiven"

import urllib
import json

google_maps_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = raw_input("Enter address: ")
encoded_url = google_maps_url + urllib.urlencode({'sensor':'false', 'address': address})
print encoded_url
map_data = urllib.urlopen(encoded_url).read()
map_data = json.loads(str(map_data))
print map_data['results'][0]['place_id']
