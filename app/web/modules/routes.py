from fastapi import APIRouter, Request
from app.web.dependencies import templates
from app.services import StepsService

router = APIRouter(
        prefix="/modules"
)


@router.get("/{stub}")
def get_module_by_stub(request: Request, stub: str):
    return templates.TemplateResponse(
        "modules/modul.html",
        context={
            "request": request,
            "stub": stub
        })