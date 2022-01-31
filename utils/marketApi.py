from binance.spot import Spot as Client
from model.exchange_info_item import Exchange_info_item
from model.historical_trades import Historical_trades_24h
from model.TradeList import Trade_list
from model.book_tickers import Book_ticker
from typing import Union, Tuple
import pandas as pd


def exchange_info_with_specific_quoteAccess(client: Client ,quoteAsset : str) -> Union[Tuple[str, pd.DataFrame], None]:
    try:
        exchange_items = client.exchange_info()["symbols"]
        
        data = []
        for item in exchange_items:
            m = Exchange_info_item.parse_obj(item)
            data.append(m)
            
        exchange_info_df = pd.DataFrame([s.__dict__ for s in data])
        # filter symbol with quote asset BTC
        condition = exchange_info_df["quoteAsset"] == quoteAsset
        return quoteAsset, exchange_info_df[condition]
    except:
        return None
    

def historical_trades_in_24hrs(client: Client) -> Union[pd.DataFrame, None]:
    try:
        historical_trades = client.ticker_24hr()
        data = []
        for trade in historical_trades:
            m = Historical_trades_24h.parse_obj(trade)
            data.append(m)
        return pd.DataFrame([s.__dict__ for s in data])
    except:
        return None

def symbols_trade_list(client: Client, symbols: list) -> Union[pd.DataFrame, None]:
    try:
        data = []
        for symbol in symbols:
            trades = client.trades(symbol)
            for trade in trades:
                trade["symbol"] = symbol
                m = Trade_list.parse_obj(trade)
                data.append(m)
        df = pd.DataFrame([s.__dict__ for s in data])
        return df
    except:
        return None
    
    
def order_book_ticker(client: Client) -> Union[pd.DataFrame, None]:
    try:
        order_book_ticker = client.book_ticker()
        data = []
        for ticker in order_book_ticker:
            m = Book_ticker.parse_obj(ticker)
            data.append(m)
        df = pd.DataFrame([s.__dict__ for s in data])
        return df
    except:
        return None
    
        