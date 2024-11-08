from fastapi import FastAPI
from srcs.auth import get_protected_docs
from srcs.routes import root
from srcs.routes import test

app = FastAPI()
get_protected_docs(app)

app.include_router(root.router)
app.include_router(test.router)