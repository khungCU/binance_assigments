'''
What is the price spread for each of the symbols from Q2?

The spread is the difference between the buy and sell prices quoted for a cryptocurrency. 
'''

from binance.spot import Spot as Client
from binance.lib.utils import config_logging
import logging
from utils.marketApi import order_book_ticker
from my_key import api_access_key, api_secret_key

from utils.marketApi import exchange_info_with_specific_quoteAccess, historical_trades_in_24hrs, order_book_ticker
from utils.transform import find_top_5, calc_price_spread_of_symbol

config_logging(logging, logging.ERROR)


#-------------------------------------------------
# Put it all together
#-----------------------------------------------
if __name__ == "__main__":
    spot_client = Client(key= api_access_key, secret= api_secret_key)
    
    top5 = find_top_5(exchange_info_with_specific_quoteAccess, historical_trades_in_24hrs, "USDT", spot_client, "count")
    
    res = calc_price_spread_of_symbol(top5, order_book_ticker, spot_client)
    
    print(res)
    
    
    
    