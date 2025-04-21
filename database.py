from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class OrmTask(Model):
    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]] = None


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def get_session():
    async with new_session() as session:
        yield session


class UserModel(Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    position: Mapped[str]


async def set_db():
    async with engine.begin() as conn:
        conn.run_sync(UserModel.metadata.drop_all)
        conn.run_sync(UserModel.metadata.create_all)
    return {"ok": True}
