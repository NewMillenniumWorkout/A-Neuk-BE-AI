from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
import secrets
import os


security = HTTPBasic()
username = os.getenv("SWAGGER_USERNAME")
password = os.getenv("SWAGGER_PASSWORD")


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, username)
    correct_password = secrets.compare_digest(credentials.password, password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def get_protected_docs(app):
    @app.get("/docs", response_class=JSONResponse)
    async def protected_docs(user: str = Depends(get_current_user)):
        return get_swagger_ui_html(openapi_url="/openapi.json", title="API Docs")

    @app.get("/openapi.json", response_class=JSONResponse)
    async def protected_openapi(user: str = Depends(get_current_user)):
        return JSONResponse(
            get_openapi(title="Your API", version="1.0.0", routes=app.routes)
        )
