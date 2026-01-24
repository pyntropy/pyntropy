
from app.settings import log, get_session
from app.domain import Module
from app.repositories import ModulesRepository


class ModulesService:
    @staticmethod
    def get_module_by_slug(slug: str):
        module = ModulesRepository.select_module_by_slug(slug)
        return module

