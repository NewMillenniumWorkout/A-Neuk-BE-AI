from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from app.utils.auth import get_protected_docs
from app.routes import root
from app.routes import test
from app.routes import chat
from app.routes import diary
from app.routes import remake

app = FastAPI()
get_protected_docs(app)

app.include_router(root.router)
app.include_router(test.router)
app.include_router(chat.router)
app.include_router(diary.router)
app.include_router(remake.router)