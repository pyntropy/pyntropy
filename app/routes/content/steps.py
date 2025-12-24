from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/{module_stub}/steps",
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/{step_stub}")
def get_step(module_stub: str, step_stub: str, request: Request):

    return templates.TemplateResponse(
        '404.html',
        {
            "request": request,
            "message": "Урок не найден"
        }
    )