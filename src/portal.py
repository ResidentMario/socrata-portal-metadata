"""
Implements the socrata-reducer Client class and the Pythonic dataset lister.
"""
import requests
import pandas as pd


def get_endpoints_using_raw_json_emission(domain):
    """
    Implements a raw HTTP GET against the entire Socrata portal for the domain in question. This method uses the
    first of the two ways of getting this information, the raw JSON endpoint.

    Parameters
    ----------
    domain: str
        A Socrata data portal domain. "data.seattle.gov" or "data.cityofnewyork.us" for example.

    Returns
    -------
    Generates a set of full portal dataset metadata in the form of a JSON-derived dict.
    """
    uri = "http://{0}/data.json".format(domain)
    r = requests.get(uri)
    r.raise_for_status()
    return r.json()


def get_endpoints_using_catalog_api(domain, token):
    """
    Implements a raw HTTP GET against the entire Socrata portal for the domain in question. This method uses the
    second of the two ways of getting this information, the catalog API.

    Parameters
    ----------
    domain: str
        A Socrata data portal domain. "data.seattle.gov" or "data.cityofnewyork.us" for example.
    token: str
        A Socrata application token. Application tokens can be registered by going onto the Socrata portal in
        question, creating an account, logging in, going to developer tools, and spawning a token.

    Returns
    -------
    Generates a set of full portal dataset metadata in the form of a JSON-derived dict.
    """
    # Token required for all requests. Providing login info instead is also possible but I didn't implement it.
    headers = {"X-App-Token": token}
    # The API will return only 100 requests at a time, it's up to you to spool the paginations to get the whole thing.
    uri = "http://api.us.socrata.com/api/catalog/v1?domains={0}&offset={1}"
    ret = []
    offset = 0
    while True:
        r = requests.get(uri.format(domain, offset), headers=headers)
        r.raise_for_status()
        data = r.json()
        ret += data['results']
        if len(data['results']) != 100:
            break
        else:
            offset += 100
    return ret


def list_endpoints(domain, token):
    """
    Lists all endpoints present on a Socrata data portal instance.

    Parameters
    ----------
    domain: str
        A Socrata data portal domain. "data.seattle.gov" or "data.cityofnewyork.us" for example.
    token: str
        A Socrata application token. Application tokens can be registered by going onto the Socrata portal in
        question, creating an account, logging in, going to developer tools, and spawning a token.

    Returns
    -------
    Socrata implements the URIs for the endpoints that it hosts as endpoint hashes. So for example the NYPD motor
    vehicle collisions dataset is hosted at:

    https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

    The first parts of the URI are helpful metadata injected on the portal into the URI, but are not actually
    necessary parts of the URI in and of themselves. This works just as well, serving a 304 Redirect to the same page:

    https://data.cityofnewyork.us/-/-/h9gi-nx95

    In other words the only part of the URI that matters is the hash at the end of it, "h9gi-nx95" in this case.

    This process returns all of the datasets' unique hashes. Note that datasets != endpoints --- endpoints returned
    by the above function include things like charts and views which are not the core datasets themselves.
    """
    data = get_endpoints_using_catalog_api(domain, token)
    return set(data[i]['link'].split('/')[-1] for i in range(len(data)))


def get_counts(domain, token):
    """
    Given the domain in question, generates counts for that domain of each of the different data types.

    Parameters
    ----------
    domain: str
        A Socrata data portal domain. "data.seattle.gov" or "data.cityofnewyork.us" for example.
    token: str
        A Socrata application token. Application tokens can be registered by going onto the Socrata portal in
        question, creating an account, logging in, going to developer tools, and spawning a token.

    Returns
    -------
    A pd.Series with counts of the different endpoint types classifiable as published public datasets.
   """
    json_endpoint_output = get_endpoints_using_raw_json_emission(domain)
    catalog_api_output = get_endpoints_using_catalog_api(domain, token)
    catalog_endpoints = [d['permalink'].split("/")[-1] for d in catalog_api_output]
    json_endpoints = [json_endpoint_output['dataset'][i]['landingPage'].split("/")[-1] for i in
                      range(len(json_endpoint_output['dataset']))]
    json_endpoint_types = []
    for i, endpoint in enumerate(json_endpoints):
        try:
            catalog_ind = catalog_endpoints.index(json_endpoints[i])
        except ValueError:
            json_endpoint_types.append("new")
        else:
            json_endpoint_types.append(catalog_api_output[catalog_ind]['resource']['type'])
    return pd.Series(json_endpoint_types).value_counts()
