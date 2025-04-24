from sqlalchemy import select
from .db import new_session
from models import OrmTask
from schemas.tasks import STask, STaskAdd
from repositories import TasksRepository


class SQLAlchemyRepTask(TasksRepository):
    @classmethod
    async def add_one(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data_dict = task.model_dump()
            task = OrmTask(**data_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(OrmTask)
            result = await session.execute(query)
            task_models = result.scalars().all()

            task_schemas = [STask.model_validate(
                task_model) for task_model in task_models]
            return task_schemas
