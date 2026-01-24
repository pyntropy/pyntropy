from uuid import uuid4
from pathlib import Path
from contextlib import asynccontextmanager


from app.settings import log, Base, engine, get_session

from .seed import seed_module
from app.models import ModuleState, ModuleModel, StepState, StepModel
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.web import router as web_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    log.info("Tables created")
    seed_module()
    yield


BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(
    title="Pyntropy",
    version="0.0.1",
    lifespan=lifespan
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "web/static"), name="static")
app.include_router(web_router)
