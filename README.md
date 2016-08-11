## README

### About

This repository contains the files, notebooks, scripts, and data output related to metadata about the [New York City
Open Data Portal](https://nycopendata.socrata.com/). The techniques and scripts here are extensible to *any*
Socrata open data portal.

For further reference, [read the accompanying blog post](http://residentmar.io/2016/08/11/nyc-open-data-portal.html).

### Contents

#### Notebooks

* `notebooks/Socrata Portal Dataset Counting.ipynb` &mdash; definitions of various Socrata dataset-related terms, and a
scoping out of ways to count them both naively and programmatically.
* `notebooks/NYC Open Data Analysis.ipynb` &mdash; Presentation and analysis of metadata about the New York City open data
portal, specifically.
* `notebook/JSON-to-Catalog API Match.ipynb` &mdash; Notebook generating the `datasets.json` file used in this
analysis. Proof of concept for the `portal` `get_datasets(domain, token)` method.

#### Modules

* `src/portal.py` &mdash; Module for working with Socrata portal metadata. Read the docstrings!

#### Scripts

* `src/load_catalog.py` &mdash; Runnable Python scripts with generates a set of metadata about endpoints (everything
on a chosen portal, including charts and other non-dataset entities) using the [Socrata Catalog API](http://labs.socrata.com/docs/search.html).
* `src/load_datasets.py` &mdash; Runnable Python scripts with generates a set of metadata about "datasets" (at
least, one definition thereof) on the open data portal.
* `src/get_dataset_counts.py` &mdash; Runnable Python scripts with generates counts of entities classifiable as
"datasets" by endpoint types.
* `src/load_datasets_using_json_endpoint.py` &mdash; Auxillary runnable Python script which generates a set of
metadata about "datasets" (at least, our definition thereof) on the open data portal using solely the portal's JSON
endpoint. `load_datasets.py`, which provides richer matched catalog API output (see the docs), is more useful.

### Further reading

Thomas Levine did a [longitudinal study of Socrata portal instances](https://thomaslevine.com/!/socrata-summary/)
well worth reading if you're into this sort of thing (there is also a post on Socrata's blog about the [aftermath](https://socrata.com/blog/my-visit-to-socrata-and-data-analysis-about-data-analysis/)
of that effort).
