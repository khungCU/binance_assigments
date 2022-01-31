'''
Using the symbols from Q1, 
what is the total notional value of the top 200 bids and asks currently on each order book?

Notional value = Contract size x Spot price
                 bidQty x bidPrice
'''
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from my_key import api_access_key, api_secret_key
import logging

from utils.marketApi import symbols_trade_list , exchange_info_with_specific_quoteAccess, historical_trades_in_24hrs
from utils.transform import calc_notional_value, find_top_5


if __name__ == "__main__":
    
    config_logging(logging, logging.ERROR)
    
    spot_client = Client(key= api_access_key, secret= api_secret_key)
    
    top5 = find_top_5(exchange_info_with_specific_quoteAccess, historical_trades_in_24hrs, "BTC", spot_client, "volume")

    calc_notional_value(top5, symbols_trade_list, spot_client)