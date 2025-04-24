from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from schemas.tasks import STask, STaskAdd, STaskId
from db.tasks import SQLAlchemyRepTask

router = APIRouter(
    prefix='/task',
    tags=['Taски']
)


@router.post('/')
async def add_task(
    task: STaskAdd
) -> STaskId:
    id = await SQLAlchemyRepTask.add_one(task)
    return {"ok": True, "id": id}


@router.get('/')
async def get_tasks() -> list[STask]:
    tasks = await SQLAlchemyRepTask.find_all()

    return tasks
