"""Communicate with the RuneLite API to get price information"""

import os
import json
import requests

# API endpoints
BASE_URL = "http://prices.runescape.wiki/api/v1/osrs"
LATEST_URL = BASE_URL + "/latest"
MAPPING_URL = BASE_URL + "/mapping"
FIVE_MIN_URL = BASE_URL + "/5m"
ONE_HOUR_URL = BASE_URL + "/1h"
TIME_SERIES_URL = BASE_URL + "/timeseries"
DAILY_VOLUMES_URL = BASE_URL + "/volumes"

# Define User-Agent
headers = requests.utils.default_headers()
headers.update({"User-Agent": os.environ.get("USER_AGENT")})

def make_request(url, params=None):
    """
    Make a request to the RuneLite API.
    :param url: API endpoint
    :param params: Parameters to specify which data to get (optional)
    :return: dict
    """
    result = requests.get(url, headers=headers, params=params)
    return json.loads(result.content)

def get_latest(item_id=None):
    """
    Get the latest high/low prices with timestamps. If item_id
    is not specified, get data for all items found by RuneLite API
    :param item_id: Item ID to get data for (optional)
    :return: dict
    """
    if item_id:
        return make_request(url=LATEST_URL, params={"id": item_id})
    return make_request(url=LATEST_URL)

def get_mapping():
    """
    Get the mappings for all items. Contains item name, id, examine text,
    members status, low alch value, high alch value, GE buy limit, and Wiki icon filename
    :return: dict
    """
    return make_request(url=MAPPING_URL)

def get_5_min(start_time=None):
    """
    Get average high and low prices and volume traded for a 5 minute period
    :param start_time: UNIX timestamp for beginning of period (optional)
    :return: dict
    """
    if start_time:
        return make_request(url=FIVE_MIN_URL, params={"timestamp": start_time})
    return make_request(url=FIVE_MIN_URL)

def get_1_hr(start_time=None):
    """
    Get average high and low prices and volume traded for a 1 hour period
    :param start_time: UNIX timestamp for beginning of period (optional)
    :return: dict
    """
    if start_time:
        return make_request(url=ONE_HOUR_URL, params={"timestamp": start_time})
    return make_request(url=ONE_HOUR_URL)

def get_timeseries(item_id, timestep):
    """
    Get a list of high and low prices and volumes
    traded for a given item over a period of time
    :param item_id: Item ID to get data for
    :param timestep: Time between data points. Options are "5m", "1h", and "6h"
    :return: dict
    """
    return make_request(url=TIME_SERIES_URL, params={"id": item_id, "timestep": timestep})

def get_volumes():
    """
    Get a list of daily trading volumes
    :return: dict
    """
    return make_request(url=DAILY_VOLUMES_URL)
    # with open("../data/volumes.json", "w") as fp:
    #     fp.write(json.dumps(make_request(url=DAILY_VOLUMES_URL)))
