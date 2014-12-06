import re
import requests

location = "http://www.ieee.org/netstorage/standards/oui.txt"
number_name = re.compile(" *(\w{6}) *\(.*\)[^\w]+(.*)$")

# Get the listing from the source location.
req = requests.get(location)

# Ignore the first 127 characters of junk data.
req_string = req.text[127:]

# Break the request string into a list of entries.
entries = req_string.split('\r\n\r\n')

for entry in entries:
    matches = number_name.search(entry.split('\r\n')[1])

    print("{}: {}".format(matches.group(2), matches.group(1)))
