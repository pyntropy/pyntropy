from fastapi import APIRouter, Request

from app.settings import log
from app.web.dependencies import templates
from app.services import ModulesService
from .steps import router as step_router
router = APIRouter(
        prefix="/modules"
)


@router.get("/{module_slug}")
def get_module_by_stub(request: Request, module_slug: str):
    log.info(f'[WEB:RQ] Запрос страницы модуля: {module_slug}')
    module = ModulesService.get_module_by_slug(module_slug)
    return templates.TemplateResponse(
        "modules/module.html",
        context={
            "request": request,
            "module": module
        })


@router.get("/{module_slug}/{step_slug}")
def get_steps(request: Request, stub: str):
    # step = StepsService.get_step_by_slug(stub)
    return True