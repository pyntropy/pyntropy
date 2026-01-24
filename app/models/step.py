from uuid import UUID
from app.domain import StepState
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings import Base




class StepModel(Base):
    __tablename__ = "steps"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    module_id: Mapped[UUID] = mapped_column(ForeignKey("modules.id"))
    state: Mapped[StepState] = mapped_column(default="draft")
    title: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True)
    overview: Mapped[str | None] = mapped_column()
    summary: Mapped[str | None] = mapped_column()

    module= relationship(
        "ModuleModel",
        back_populates="steps",
        uselist=False
    )

    def __repr__(self):
        return f'{self.title}'