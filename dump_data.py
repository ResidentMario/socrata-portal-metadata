"""
Small command-line script which dumps all Socrata endpoints into a local file.
"""

from portal import get_endpoints
import json

domain = input("Domain: ")
key = input("Key: ")
portal_contents = get_endpoints(domain, key)
with open("portal_contents_raw.json", "w") as f:
    f.write(json.dumps(portal_contents, indent=4))