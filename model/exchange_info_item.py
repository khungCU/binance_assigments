from pydantic import BaseModel


# -------------------------------------------------
# exchange info
# -------------------------------------------------
class Exchange_info_item(BaseModel):
    symbol: str
    status: str
    baseAsset: str
    quoteAsset: str
