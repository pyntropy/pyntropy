from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.services import StepsService

router = APIRouter(
        prefix="/steps"
)


@router.get("/")
def get_steps():
    return HTMLResponse(content=StepsService.get_step())