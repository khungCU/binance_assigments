"""
Print the top 5 symbols with quote asset USDT and
the highest number of trades over the last 24 hours in descending order.
"""
import logging

from binance.lib.utils import config_logging
from binance.spot import Spot as Client

from my_key import api_access_key
from my_key import api_secret_key
from utils.marketApi import exchange_info_with_specific_quoteAccess
from utils.marketApi import historical_trades_in_24hrs
from utils.transform import find_top_5

config_logging(logging, logging.ERROR)


# -------------------------------------------------
# Put it all together
# -----------------------------------------------
if __name__ == "__main__":
    spot_client = Client(key=api_access_key, secret=api_secret_key)
    find_top_5(
        exchange_info_with_specific_quoteAccess,
        historical_trades_in_24hrs,
        "USDT",
        spot_client,
        "count",
    )
