from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

# роутеры запросов
from app.routers.main import router as main_router
from app.routers.content.steps import router as step_router

app = FastAPI(
    title='Pyntropy',
    description='Обучение системных аналитиков.',
    version='0.0.1')

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(main_router)
app.include_router(step_router)


