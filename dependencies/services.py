from typing import Annotated

from fastapi import Depends
from repositories.sqlalchemy_tasks import SQLAlchemyTasksRep
from repositories.sqlalchemy_users import SQLAlchemyUsersRep
from services import UsersService, TaskService


def task_service():
    return TaskService(SQLAlchemyTasksRep)


def user_service():
    return UsersService(SQLAlchemyUsersRep)


UsersServiceDep = Annotated[UsersService, Depends(user_service)]
TaskServiceDep = Annotated[TaskService, Depends(task_service)]
