from pydantic import BaseModel


# -------------------------------------------------
# all orders
# -------------------------------------------------
class All_orders(BaseModel):
    symbol: str
    orderId: str
    price: str
    origQty: str
    time: int
    updateTime: int
    isWorking: bool
