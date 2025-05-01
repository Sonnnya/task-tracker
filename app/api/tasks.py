from fastapi import APIRouter
from schemas.tasks import STask, STaskAdd, STaskId
from dependencies import SessionDep, TaskServiceDep

router = APIRouter(
    prefix='/task',
    tags=['Taски']
)


@router.post('/')
async def add_task(
    task: STaskAdd,
    session: SessionDep,
    task_service: TaskServiceDep
) -> STaskId:
    id = await task_service.add_one(session, task)
    return {"ok": True, "id": id}


@router.get('/')
async def get_tasks(session: SessionDep, task_service: TaskServiceDep) -> list[STask]:
    return await task_service.get_all(session)
