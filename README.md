This repository contains the files, notebooks, scripts, and data output related to metadata about the [New York City
Open Data Portal](https://nycopendata.socrata.com/). The techniques and scripts here are extensible to *any*
Socrata open data portal.

## Contents

Excluding disinteresting stuff.

### Notebooks

* `notebooks/Socrata Portal Dataset Counting.ipynb` &mdash; definitions of various Socrata dataset-related terms, and a
scoping out of ways to count them both naively and programmatically.
* `notebooks/NYC Open Data Analysis.ipynb` &mdash; Presentation and analysis of metadata about the New York City open data
portal, specifically.

### Modules

* `src/portal.py` &mdash; Module for working with Socrata portal metadata.

### Scripts

* `src/load_catalog.py` &mdash; Runnable Python scripts with generates a set of metadata about endpoints (everything
on a chosen portal, including charts and other non-dataset entities) using the [Socrata Catalog API](http://labs.socrata.com/docs/search.html).
* `src/load_endpoints.py` &mdash; Runnable Python scripts with generates a set of metadata about "datasets" (at
least, one definition thereof) on the open data portal.
* `src/get_dataset_counts.py` &mdash; Runnable Python scripts with generates counts of entities classifiable as
"datasets" by endpoint types.

## Further reading

Read `notebooks/Socrata Portal Dataset Counting.ipynb` to get an understanding of why counting so-called datasets on
a Socrata portal is a non-trivial task (blog post forthcoming). You can then read the comments in the `src/portal.py`
source code to get a technical understanding of what the two endpoints used in this project (the Catalog API and
the JSON endpoint) are, and why both are necessary.