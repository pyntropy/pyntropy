from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic.v1 import parse_raw_as


def get_modules_page(request: Request):
    """
    Метод не принимает параметров.

    :return: Страницу со списком обучающих модулей.
    """
    pass


def get_module_page(module_stub: str, request: Request):
    """

    :param module_stub: id модуля в текстовом формате.
    :param request:
    :return: Страницу со списком уроков для выбранного модуля.
    """
    # TODO: метод запрашивает данные модуля из SQLLite
    pass


