from pydantic import BaseModel


#-------------------------------------------------
#  Historical trades in 24h
#------------------------------------------------
class Historical_trades_24h(BaseModel): 
    symbol: str
    priceChange: float
    priceChangePercent: float
    prevClosePrice: float
    lastPrice: float
    bidPrice: float
    bidQty: float
    askPrice: float
    openPrice: float
    highPrice: float
    lowPrice: float
    volume: float
    quoteVolume: float
    openTime: int
    closeTime: int
    firstId: int
    lastId: int
    count: int
    
#-------------------------------------------------
# old trade lookup
#------------------------------------------------
class Historical_trades(BaseModel):
    symbol: str
    id: int
    price: float
    qty: float
    quoteQty: float
    time: int