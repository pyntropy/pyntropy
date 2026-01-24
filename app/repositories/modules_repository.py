from app.settings import get_session
from app.models import ModuleModel
from app.domain import Module, Step


class Mapper:
    @staticmethod
    def to_domain(module_orm: ModuleModel):
        # Преобразуем каждый StepModel в доменный объект Step
        steps = [
            Step(
                id=step_orm.id,
                module_id=step_orm.module_id,
                state=step_orm.state,
                title=step_orm.title,
                slug=step_orm.slug,
                overview=step_orm.overview,
                summary=step_orm.summary
            )
            for step_orm in module_orm.steps
        ]
        
        module = Module(
            id=module_orm.id,
            state=module_orm.state,
            title=module_orm.title,
            slug=module_orm.slug,
            overview=module_orm.overview,
            summary=module_orm.summary,
            steps=steps
        )
        return module


class ModulesRepository:
    @staticmethod
    def select_module_by_slug(slug: str):
        with get_session() as session:
            module_orm = session.query(ModuleModel).filter(ModuleModel.slug == slug).first()
            module = Mapper.to_domain(module_orm)
            return module
