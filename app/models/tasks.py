from sqlalchemy.orm import Mapped
from .abstract_model import Model
from typing import Optional


class OrmTask(Model):
    __tablename__ = 'Tasks'

    name: Mapped[str]
    description: Mapped[Optional[str]] = None
