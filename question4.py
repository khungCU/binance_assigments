"""
What is the price spread for each of the symbols from Q2?
The spread is the difference between the buy
and sell prices quoted for a cryptocurrency.
"""
import logging

from binance.lib.utils import config_logging
from binance.spot import Spot as Client

from my_key import api_access_key
from my_key import api_secret_key
from utils.marketApi import exchange_info_with_specific_quoteAccess
from utils.marketApi import historical_trades_in_24hrs
from utils.marketApi import order_book_ticker
from utils.transform import calc_price_spread_of_symbol
from utils.transform import find_top_5

config_logging(logging, logging.ERROR)


# -------------------------------------------------
# Put it all together
# -----------------------------------------------
if __name__ == "__main__":
    spot_client = Client(key=api_access_key, secret=api_secret_key)

    top5 = find_top_5(
        exchange_info_with_specific_quoteAccess,
        historical_trades_in_24hrs,
        "USDT",
        spot_client,
        "count",
    )

    res = calc_price_spread_of_symbol(top5, order_book_ticker, spot_client)

    print(res)
