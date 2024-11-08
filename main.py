from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from srcs.auth import get_protected_docs, get_current_user

app = FastAPI()

get_protected_docs(app)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class ItemResponse(BaseModel):
    item_id: int
    item_name: str
    item_price: float
    item_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def read_test():
    return "fastapi api content"


@app.get("/test-auth")
def read_test(user: str = Depends(get_current_user)):
    return "fastapi api auth content"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    return ItemResponse(
        item_id=item_id,
        item_name=item.name,
        item_price=item.price,
        item_offer=item.is_offer,
    )
