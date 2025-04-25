from dependencies.common import SessionDep
from repositories import TasksRepository
from schemas.tasks import STaskAdd


class TaskService():
    def __init__(self, task_repo: TasksRepository):
        self.repo = task_repo()

    async def add_one(self, session: SessionDep, user: STaskAdd):
        id = await self.repo.add_one(session, user)
        return id

    async def get_all(self, session: SessionDep):
        return await self.repo.get_all(session)
