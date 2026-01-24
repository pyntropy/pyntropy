from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.services import StepsService

router = APIRouter(
        prefix="/"
)


