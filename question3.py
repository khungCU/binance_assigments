"""
Using the symbols from Q1,
what is the total notional value of the top
200 bids and asks currently on each order book?

Notional value = Contract size x Spot price
                 bidQty x bidPrice
"""
import logging

from binance.lib.utils import config_logging
from binance.spot import Spot as Client

from my_key import api_access_key
from my_key import api_secret_key
from utils.marketApi import exchange_info_with_specific_quoteAccess
from utils.marketApi import historical_trades_in_24hrs
from utils.marketApi import symbols_trade_list
from utils.transform import calc_notional_value
from utils.transform import find_top_5


if __name__ == "__main__":

    config_logging(logging, logging.ERROR)

    spot_client = Client(key=api_access_key, secret=api_secret_key)

    top5 = find_top_5(
        exchange_info_with_specific_quoteAccess,
        historical_trades_in_24hrs,
        "BTC",
        spot_client,
        "volume",
    )

    calc_notional_value(top5, symbols_trade_list, spot_client)
