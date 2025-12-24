from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.repository.content.steps_repository import get_steps
from app.models.breadcrumbs import Breadcrumbs
from app.app_logger import logger

from app.routes import steps_router

app = FastAPI(
    title="Pyntropy"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(steps_router)
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    step = get_steps()
    logger.info(step)
    breadcrumbs = Breadcrumbs(
        level1="Home",
        level2="Steps"
    )
    return templates.TemplateResponse(
        "step.html", {
            "request": request,
            "breadcrumbs": breadcrumbs,
            "step": step
        }
    )


@app.get("/health")
def health():
    return {"status": "ok"}