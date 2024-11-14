from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

load_dotenv()

from src.utils.auth import get_protected_docs
from src.routes import root
from src.routes import test
from src.routes import chat
from src.routes import diary
from src.routes import remake

app = FastAPI()
get_protected_docs(app)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.include_router(root.router)
app.include_router(test.router)
app.include_router(chat.router)
app.include_router(diary.router)
app.include_router(remake.router)