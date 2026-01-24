from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.settings import Base
from app.domain import ModuleState
from .step import StepModel




class ModuleModel(Base):
    __tablename__ = "modules"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    state: Mapped[ModuleState] = mapped_column(default='draft')
    title: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True)
    overview: Mapped[str | None] = mapped_column()
    summary: Mapped[str | None] = mapped_column()

    steps: Mapped[list[StepModel]] = relationship(
        "StepModel",
        back_populates="module",
        lazy="joined",
        order_by=StepModel.title,
    )

    def __repr__(self):
        return f'{self.title}'
