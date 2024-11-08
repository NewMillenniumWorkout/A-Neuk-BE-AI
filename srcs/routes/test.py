from fastapi import APIRouter
from typing import Union
from fastapi import Depends
from srcs.auth import get_current_user
from srcs.models.test_item import TestItemResponse, TestItem

router = APIRouter(prefix="/test", tags=["Test"])


@router.get("/")
def read_test():
    return "fastapi api content"


@router.get("/auth")
def read_test(user: str = Depends(get_current_user)):
    return "fastapi api auth content"


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.post("/items/{item_id}", response_model=TestItemResponse)
def update_item(item_id: int, item: TestItem):
    return TestItemResponse(
        item_id=item_id,
        item_name=item.name,
        item_price=item.price,
        item_offer=item.is_offer,
    )
