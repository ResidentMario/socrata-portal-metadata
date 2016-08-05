from portal import get_counts
import pandas as pd

domain = input("Your Socrata domain URI: ")
key = input("Your Socrata application token: ")
filename = input("The filename you want to save this output to: ")
portal_counts = get_counts(domain, key)
portal_counts.to_csv(filename)