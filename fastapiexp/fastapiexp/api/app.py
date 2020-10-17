from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from fastapiexp.infrastructure.environments import get_environments

from .routers import form, predict


async def index():
    return FileResponse(str(Path(get_environments().public_dir) / "index.html"))


def create_app() -> FastAPI:
    app = FastAPI()
    api_router = APIRouter()
    api_router.include_router(predict.router, prefix="/predict")
    api_router.include_router(form.router, prefix="/form")
    app.include_router(api_router, prefix="/api")
    app.add_api_route("/", index, methods=["GET"])
    app.mount(
        "/public", StaticFiles(directory=get_environments().public_dir), name="public"
    )
    return app
