from fastapi import APIRouter, Depends
from schemas import SUserAdd, SUserId, SPagination
from typing import Annotated
from database import get_session, UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def add_user(user: Annotated[SUserAdd, Depends()], session: SessionDep):
    new_user = UserModel(**(user.model_dump()))
    session.add(new_user)
    await session.commit()


@router.get('/')
async def get_users(session: SessionDep):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()


PaginationDep = Annotated[SPagination, Depends(SPagination)]


@router.get('/pages')
async def get_users_pagination(
        session: SessionDep,
        pagination_dep: PaginationDep
) -> list[SUserId]:
    query = (
        select(UserModel)
        .limit(pagination_dep.limit)
        .offset(pagination_dep.offset)
    )
    result = await session.execute(query)
    return result.scalars().all()
