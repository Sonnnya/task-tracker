from fastapi import APIRouter
from schemas.tasks import STask, STaskAdd, STaskId
from db.tasks import SQLAlchemyTasksRep
from dependencies import SessionDep

router = APIRouter(
    prefix='/task',
    tags=['Taски']
)


@router.post('/')
async def add_task(
    task: STaskAdd,
    session: SessionDep
) -> STaskId:
    id = await SQLAlchemyTasksRep().add_one(session, task)
    return {"ok": True, "id": id}


@router.get('/')
async def get_tasks(session: SessionDep) -> list[STask]:
    tasks = await SQLAlchemyTasksRep().find_all(session)

    return tasks
