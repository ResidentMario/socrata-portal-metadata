"""
Small command-line script which uses the raw JSON endpoint to query for every endpoint in the chosen domain.
"""

import json

from src.portal import get_endpoints_using_raw_json_emission

domain = input("Your Socrata domain URI: ")
filename = input("The filename you want to save this output to: ")
portal_contents = get_endpoints_using_raw_json_emission(domain)
with open(filename, "w") as f:
    f.write(json.dumps(portal_contents, indent=4))
