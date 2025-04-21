from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .abstract_model import Model
from typing import Optional


class OrmTask(Model):
    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]] = None
