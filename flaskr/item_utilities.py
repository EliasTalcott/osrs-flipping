"""Utilities for operating on item data"""

import json

MAPPING_FILE = "data/mapping.json"
SETS_NAME_FILE = "data/item_sets_name.json"
SETS_ID_FILE = "data/item_sets_id.json"
VOLUMES_FILE = "data/volumes.json"

# Load mapping of items to IDs, buy limits, alch values, etc.
with open(MAPPING_FILE) as fp:
    mapping = fp.read()
mapping = json.loads(mapping)

# Load daily volumes for each item
with open(VOLUMES_FILE) as fp:
    volumes = fp.read()
volumes = json.loads(volumes)

def get_item_sets_id():
    """
    Read item sets into dictionary using item ID
    :return: Dictionary of item sets by item ID
    """
    with open(SETS_ID_FILE) as sets_file:
        sets = sets_file.read()
    return json.loads(sets)

def get_item_sets_name():
    """
    Read item sets into dictionary using item name
    :return: Dictionary of item sets by item name
    """
    with open(SETS_NAME_FILE) as sets_file:
        sets = sets_file.read()
    return json.loads(sets)

def get_id_from_name(item_name):
    """
    Returns an item's ID given its name
    :param item_name: Name of item
    :return: ID of item
    """
    try:
        return next(item for item in mapping if item["name"].lower() == item_name.lower())["id"]
    except StopIteration:
        return None

def get_name_from_id(item_id):
    """
    Returns an item's name given its ID
    :param item_id: ID of item
    :return: Name of item
    """
    try:
        return next(item for item in mapping if item["id"] == item_id)["name"]
    except StopIteration:
        return None

def get_buy_limit_from_id(item_id):
    """
    Returns an item's buy limit given its ID
    :param item_id: ID of item
    :return: Buy limit of item
    """
    try:
        return next(item for item in mapping if item["id"] == item_id)["limit"]
    except StopIteration:
        return None

def get_buy_limit_from_name(item_name):
    """
    Returns an item's buy limit given its name
    :param item_name: Name of item
    :return: Buy limit of item
    """
    try:
        return next(item for item in mapping if item["name"].lower() == item_name.lower())["limit"]
    except (StopIteration, KeyError):
        return None

def get_volume_from_id(item_id):
    """
    Returns an item's daily volume given its ID
    :param item_id: ID of item
    :return: Daily volume of item
    """
    return volumes["data"][str(item_id)]

def get_volume_from_name(item_name):
    """
    Returns an item's daily volume given its name
    :param item_name: Name of item
    :return: Daily volume of item
    """
    item_id = get_id_from_name(item_name)
    return get_volume_from_id(item_id)
