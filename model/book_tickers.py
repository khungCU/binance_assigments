from pydantic import BaseModel

#-------------------------------------------------
# Book ticker
#-------------------------------------------------
class Book_ticker(BaseModel): 
    symbol: str
    bidPrice: float
    bidQty: float
    askPrice: float
    askQty: float