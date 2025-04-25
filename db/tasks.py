from sqlalchemy import select
from .session import new_session
from models import OrmTask
from schemas.tasks import STask, STaskAdd
from repositories import TasksRepository
from dependencies import SessionDep


class SQLAlchemyTasksRep(TasksRepository):
    model = OrmTask

    async def add_one(self, session: SessionDep, task: STaskAdd) -> int:
        task = task.model_dump()
        task = self.model(**task)

        session.add(task)
        await session.flush()
        await session.commit()
        return task.id

    async def find_all(self, session: SessionDep) -> list[STask]:
        query = select(self.model)
        result = await session.execute(query)
        task_models = result.scalars().all()

        task_schemas = [STask.model_validate(
            task_model) for task_model in task_models]
        return task_schemas
