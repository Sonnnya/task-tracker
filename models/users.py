from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .abstract_model import Model


class OrmUser(Model):
    __tablename__ = 'users'

    name: Mapped[str]
    position: Mapped[str]
