from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from models import Model
from models import OrmTask
from models import UserModel

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def get_session():
    async with new_session() as session:
        yield session


async def set_db():
    async with engine.begin() as conn:
        conn.run_sync(UserModel.metadata.drop_all)
        conn.run_sync(UserModel.metadata.create_all)
    return {"ok": True}
