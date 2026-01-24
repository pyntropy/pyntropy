from uuid import UUID
from enum import StrEnum


class StepState(StrEnum):
    DRAFT = "draft"


class Step:
    id: UUID
    module_id: UUID
    state: StepState
    title: str
    slug: str
    overview: str | None
    summary: str | None

    def __init__(self, id, module_id, state, title, slug, overview, summary):
        self.id = id
        self.module_id = module_id
        self.state = state
        self.title = title
        self.slug = slug
        self.overview = overview
        self.summary = summary
