from uuid import UUID
from enum import StrEnum
from .step import Step


class ModuleState(StrEnum):
    DRAFT = "draft"


class Module:
    id: UUID
    state: ModuleState
    title: str
    slug: str
    overview: str
    summary: str
    steps: list[Step]

    def __init__(self, id, state, title, slug, overview, summary, steps: list[Step] = None):
        self.id = id
        self.state = state
        self.title = title
        self.slug = slug
        self.overview = overview
        self.summary = summary
        self.steps = steps
