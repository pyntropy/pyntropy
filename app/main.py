from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.web import modules_router, base_router, steps_router

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "web/static"), name="static")
app.include_router(base_router)
app.include_router(modules_router)
app.include_router(steps_router)



# @app.get("/")
# def home(request: Request):
#     return templates.TemplateResponse(
#         "base.html", {
#             "request": request
#         })