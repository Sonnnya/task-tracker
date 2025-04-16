from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from schemas import STask, STaskAdd, STaskId
from repository import RepTask

router = APIRouter(
    prefix='/task',
    tags=['Taски']
)


@router.post('/')
async def add_task(
    task: STaskAdd
) -> STaskId:
    id = await RepTask.add_one(task)
    return {"ok": True, "id": id}


@router.get('/')
async def get_tasks() -> list[STask]:
    tasks = await RepTask.find_all()

    return tasks
