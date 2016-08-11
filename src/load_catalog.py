"""
Small command-line script which uses the catalog API to query for every endpoint in the chosen domain. Saves the raw
output to disc locally.
"""

import json

from src.portal import get_endpoints_using_catalog_api

domain = input("Your Socrata domain URI: ")
key = input("Your Socrata application token: ")
filename = input("The filename you want to save this output to: ")
portal_contents = get_endpoints_using_catalog_api(domain, key)
with open(filename, "w") as f:
    f.write(json.dumps(portal_contents, indent=4))