from fastapi import FastAPI

from .routers import form, predict


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(predict.router, prefix="/predict")
    app.include_router(form.router, prefix="/form")
    return app
