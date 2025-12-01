from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers.main import main_router


app = FastAPI(
    title='Pyntropy',
    description='Курсы по ИТ для системных аналитиков.',
    version='0.0.1')

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(main_router)



