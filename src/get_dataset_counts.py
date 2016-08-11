"""
Small command-line script which uses the two metadata endpoints (the Catalog API and the raw JSON output) to generate
and save a file with dataset entity counts (see `portal.get_counts` for more semantic information).

This script provides a subset of the information provided by `load_datasets.py`.
"""

from portal import get_counts

domain = input("Your Socrata domain URI: ")
key = input("Your Socrata application token: ")
filename = input("The filename you want to save this output to: ")
portal_counts = get_counts(domain, key)
portal_counts.to_csv(filename)