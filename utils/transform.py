import pandas as pd
from typing import Callable, Union
from binance.spot import Spot as Client
from utils.msg import volume_msg, count_msg

#-------------------------------------------------
# 1. Inner Join  exchange info with historical_trades_in_24hrs
# 2. Order by volumes DESC
# 3. HEAD 5
# 4. Print out result
#-----------------------------------------------

def output_msg(input: str) -> str:
    if input == "count":
        return count_msg["msg"]
    elif input == "volume":
        return volume_msg["msg"]
    else:
        assert Exception("output_msg took unsupport parameter")


def find_top_5(exchange_info_with_specific_quoteAccess: Callable, historical_trades_in_24hrs: Callable, quoteasset: str, client: Client, option: str) -> Union[list, None]:
    '''
    option support volume, count 
    '''
    
    quoteAsset, exchange_info_df = exchange_info_with_specific_quoteAccess(client, quoteasset)
    historical_trades_df = historical_trades_in_24hrs(client)
    
    if isinstance(exchange_info_df, pd.DataFrame) and isinstance(historical_trades_df, pd.DataFrame):
        merged_df = exchange_info_df.merge(historical_trades_df , on=["symbol"],how="inner")\
                                    .sort_values(by=[option], ascending=False)\
                                    .head(5)          
        print(f"Printing the top 5 symbols with quote asset {quoteAsset} and the highest {output_msg(option)} over the last 24 hours in descending order.")
        print(merged_df[["symbol", option]].reset_index(drop=True))
        
        return merged_df["symbol"].tolist()
    else:
        assert Exception("Things not working")
        

def calc_notional_value(symbols:list,  symbols_trade_list: Callable, client: Client) ->  Union[pd.DataFrame, None]:
    df_symbols_trade_list = symbols_trade_list(client, symbols)
    
    if isinstance(df_symbols_trade_list, pd.DataFrame):
        df_symbols_trade_list = df_symbols_trade_list.sort_values(['price'],ascending=False).groupby('symbol').head(200)
        df_symbols_trade_list["notionalValue"] = df_symbols_trade_list["price"] * df_symbols_trade_list["qty"]
        df_total_notional_value = df_symbols_trade_list.groupby("symbol").sum("notionalValue").reset_index()
        df_total_notional_value = df_total_notional_value[["symbol", "notionalValue"]]
        print("Using the symbols from Q1, The total notional value of the top 200 bids and asks currently on each order book")
        print(df_total_notional_value)
        return df_total_notional_value
    else:
        assert Exception("Things not working")
        
def calc_price_spread_of_symbol(symbols: list, order_book_ticker: Callable ,client: Client) -> Union[pd.DataFrame, None]:
    
    df_order_book_ticker = order_book_ticker(client)
    
    if isinstance(df_order_book_ticker, pd.DataFrame):
        cond = df_order_book_ticker["symbol"].str.contains('|'.join(symbols))
        df_order_book_ticker = df_order_book_ticker[cond]
        df_order_book_ticker["price_spread"] = df_order_book_ticker["bidPrice"] - df_order_book_ticker["askPrice"]
        
        df_order_book_ticker = df_order_book_ticker[["symbol", "price_spread"]]
        return df_order_book_ticker
    else:
        assert Exception("Things not working")
