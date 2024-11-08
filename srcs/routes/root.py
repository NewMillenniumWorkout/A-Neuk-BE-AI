from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_root():
    return {"aneuk": "Hello aneuk ai world...!"}
