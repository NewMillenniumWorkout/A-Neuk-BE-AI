from pydantic import BaseModel
from typing import Union


class TestItem(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class TestItemResponse(BaseModel):
    item_id: int
    item_name: str
    item_price: float
    item_offer: Union[bool, None] = None
