from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from srcs.auth import get_protected_docs
from srcs.routes import root
from srcs.routes import test
from srcs.routes import chat

app = FastAPI()
get_protected_docs(app)

app.include_router(root.router)
app.include_router(test.router)
app.include_router(chat.router)
