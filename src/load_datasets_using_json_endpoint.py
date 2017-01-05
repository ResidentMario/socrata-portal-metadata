"""
Small command-line script which uses the raw JSON endpoint to query for every endpoint in the chosen domain. Saves
the raw output to disc locally.

In general this script provides a subset of the data provided by `load_datasets.py`.
"""

import json
from portal import get_endpoints_using_raw_json_emission

domain = input("Your Socrata domain URI: ")
filename = input("The filename you want to save this output to: ")
portal_contents = get_endpoints_using_raw_json_emission(domain)
with open(filename, "w") as f:
    f.write(json.dumps(portal_contents, indent=4))
