from pydantic import BaseModel


class Trade_list(BaseModel):
    symbol: str
    id: int
    price: float
    qty: float
    quoteQty: float
    time: float
    isBuyerMaker: bool
    isBestMatch: bool
