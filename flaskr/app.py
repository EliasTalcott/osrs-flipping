"""Flask application to present flipping information"""

import locale
from time import time
from flask import Flask, render_template
from flaskr.runelite_api import get_latest
from flaskr.item_utilities import get_buy_limit_from_name, get_item_sets_name, get_id_from_name, \
    get_volume_from_name
from flaskr.profit import calc_profit_roi

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, "en_US.UTF8")

@app.route("/")
def hello():
    """
    Homepage. Will eventually include buttons to
    navigate to various flipping utility pages
    :return: Welcome message
    """
    return "Welcome to my OSRS flipping utility!"

@app.route('/sets_to_components')
def item_sets_to_components():
    """
    Show the most recent profit and ROI
    for separating sets into their components
    :return: Sorted table of profit/ROI values
    """
    # Get most recent prices
    latest = get_latest()

    # Fill in set profit data
    headings = ["Set", "Components", "Set Price", "Components Price", "Margin",
                "ROI (%)", "Buy Limit", "Daily Volume", "Margin * Buy Limit"]
    sets = get_item_sets_name()
    data = []
    start = time()
    try:
        for key, val in sets.items():
            set_cost = latest["data"][str(get_id_from_name(key))]["high"]
            components = ""
            components_cost = 0
            for comp in val["components"]:
                components += comp + ", "
                components_cost += latest["data"][str(get_id_from_name(comp))]["low"]
            margin, roi = calc_profit_roi(set_cost, components_cost)
            buy_limit = min([get_buy_limit_from_name(val) for val in val["components"]])
            data.append([key, components[:-2], format(set_cost, ",d"),
                         format(components_cost, ",d"), format(int(margin), ",d"), roi.__round__(1),
                         format(buy_limit, ",d"), get_volume_from_name(key),
                         format(int(margin * buy_limit), ",d")])
    except TypeError:
        print("Could not add data for {}".format(key))
    # Sort by Margin * Buy Limit
    # data.sort(key=lambda x: locale.atoi(x[5]), reverse=True)
    # Sort by ROI
    data.sort(key=lambda x: x[5], reverse=True)
    print("Time to load all stuff: {}".format(time() - start))

    # Calculate profit
    return render_template("item_sets.html", headings=headings, data=data)
