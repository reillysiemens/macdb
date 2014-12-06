import re
import hashlib
import requests

location = "http://www.ieee.org/netstorage/standards/oui.txt"
number_name = re.compile(" *(\w{6}) *\(.*\)[^\w]+(.*)$")
oui_hash = hashlib.sha1()
companies = []

# Get the listing from the source location.
req = requests.get(location)

# Update our hash object with the value from our request string.
oui_hash.update(bytes(req.text, "utf-8"))

# Ignore the first 127 characters of junk data.
req_string = req.text[127:]

# Break the request string into a list of entries.
entries = req_string.split('\r\n\r\n')

# Remove junk entry at the end.
del entries[-1]

for entry in entries:
    lines = entry.split('\r\n')
    matches = number_name.search(lines[1])
    company = {'name': matches.group(2), 'oui': matches.group(1)}
    companies.append(company)
