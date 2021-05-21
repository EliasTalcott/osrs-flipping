"""Calculate profit and ROI given single items or lists of items"""

def calc_profit_roi(buy, sell):
    """
    Calculate the profit and ROI (%) from
    buying and selling an item or items
    :param buy: Single price or list or prices to buy
    :param sell: Single price or list of prices to sell
    :return: Tuple of profit and ROI floats
    """
    # Calculate total price of item(s) to buy
    if isinstance(buy, list):
        buy_price = float(sum(buy))
    else:
        buy_price = float(buy)

    # Calculate total price of item(s) to sell
    if isinstance(sell, list):
        sell_price = float(sum(sell))
    else:
        sell_price = float(sell)

    # Calculate profit and ROI
    profit = sell_price - buy_price
    roi = (profit / buy_price) * 100
    return profit, roi
