"""
Small command-line script which uses the raw JSON endpoint to query for every endpoint in the chosen domain. Saves
the raw output to disc locally.
"""

import json

from portal import get_datasets

domain = input("Socrata URI (e.g. 'data.cityofnewyork.us'): ")
key = input("Socrata application token: ")
filename = input("Output filename (e.g. 'mydata.json'): ")
datasets = get_datasets(domain, key)
with open(filename, "w") as f:
    f.write(json.dumps(datasets, indent=4))