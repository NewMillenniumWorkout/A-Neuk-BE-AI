from fastapi import FastAPI
from dotenv import load_dotenv
from srcs.auth import get_protected_docs
from srcs.routes import root
from srcs.routes import test


app = FastAPI()
load_dotenv()
get_protected_docs(app)

app.include_router(root.router)
app.include_router(test.router)
