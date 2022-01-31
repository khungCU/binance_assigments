'''
Print the top 5 symbols with quote asset BTC and the highest volume over the last 24 hours in descending order.
'''
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
import logging
from my_key import api_access_key, api_secret_key

from utils.marketApi import exchange_info_with_specific_quoteAccess, historical_trades_in_24hrs
from utils.transform import find_top_5

config_logging(logging, logging.ERROR)


#-------------------------------------------------
# Put it all together
#-----------------------------------------------
if __name__ == "__main__":
    spot_client = Client(key= api_access_key, secret= api_secret_key)
    find_top_5(exchange_info_with_specific_quoteAccess, historical_trades_in_24hrs, "BTC", spot_client, "volume")
