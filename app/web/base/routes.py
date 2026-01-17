from pathlib import Path
from fastapi import APIRouter, Request
from app.web.dependencies import templates

router = APIRouter(
    prefix=""
)


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "base.html",
        context={
            "request": request
        })
