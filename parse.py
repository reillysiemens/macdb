import re
import hashlib
import requests

import models

location = "http://www.ieee.org/netstorage/standards/oui.txt"
oui_id = re.compile(" *(\w{6}) *\(.*\)[^\w]+(.*)$")
request_hash = hashlib.sha1()
organizations = []

# Get the listing from the source location.
request = requests.get(location)

# Update our hash object with the value from our request string.
request_hash.update(bytes(request.text, "utf-8"))

# Ignore the first 127 characters of junk data.
request_string = request.text[127:]

# Break the request string into a list of entries.
entries = request_string.split('\r\n\r\n')

# Remove junk entry at the end.
del entries[-1]

# For each entry...
for entry in entries:

    # Break the entry into lines.
    lines = entry.split('\r\n')

    # Find the id and oui for the organization.
    matches = oui_id.search(lines[1])

    # Find the address for the organization.
    address = re.sub('\s+', ' ', ' '.join(lines[2:]).strip())

    organization = models.Organization(oui=matches.group(1),
                                       name=matches.group(2),
                                       address=address)
    models.session.add(organization)

models.session.commit()
