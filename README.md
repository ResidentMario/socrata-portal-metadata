## README

### About

This repository contains the files, notebooks, scripts, and data output related to metadata about the [New York City
Open Data Portal](https://nycopendata.socrata.com/). The techniques and scripts here are extensible to *any*
Socrata open data portal.

The goal of this project was twofold. First of all, I wanted to get an understanding of how many datasets there are
on the New York City Open Data portal and what they look like. Second, I wanted to routinize this processing logic
into a few pieces of code, with the goal of making this analysis reproducible at a later time and possibly on
different portals.

The accompanying blog post (WIP) explains how this was done and what was found. It itself is based on two notebooks
in this repository, `notebooks/Socrata Portal Dataset Counting.ipynb` and `notebooks/NYC Open Data Analysis.ipynb`.

To see the presentation of outcomes, read that.

To analyze the portal or another portal yourself, read that, then read the comments in the src/portal.py source code
to get a technical understanding of what the two endpoints used in this project (the Catalog API and the JSON
endpoint) are and why both are necessary, and then look at/run `src/load_endpoints.py` and `src/load_datasets.py`
from the command line to pull down your own data and get going.

PS: Thomas Levine (separately) did a [longitudinal study of Socrata portal instances](https://thomaslevine.com/!/socrata-summary/)
well worth reading if you're into this sort of thing (there is also a post on Socrata's blog about the [aftermath](https://socrata.com/blog/my-visit-to-socrata-and-data-analysis-about-data-analysis/)
of that effort).

### Contents

Excluding disinteresting stuff.

#### Notebooks

* `notebooks/Socrata Portal Dataset Counting.ipynb` &mdash; definitions of various Socrata dataset-related terms, and a
scoping out of ways to count them both naively and programmatically.
* `notebooks/NYC Open Data Analysis.ipynb` &mdash; Presentation and analysis of metadata about the New York City open data
portal, specifically.

#### Modules

* `src/portal.py` &mdash; Module for working with Socrata portal metadata.

#### Scripts

* `src/load_catalog.py` &mdash; Runnable Python scripts with generates a set of metadata about endpoints (everything
on a chosen portal, including charts and other non-dataset entities) using the [Socrata Catalog API](http://labs.socrata.com/docs/search.html).
* `src/load_datasets.py` &mdash; Runnable Python scripts with generates a set of metadata about "datasets" (at
least, one definition thereof) on the open data portal.
* `src/get_dataset_counts.py` &mdash; Runnable Python scripts with generates counts of entities classifiable as
"datasets" by endpoint types.