from fastapi import APIRouter, Depends
from schemas.users import SUserAdd, SUserId, SPagination
from typing import Annotated
from db.db import get_session, UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def add_user(user: SUserAdd, session: SessionDep):
    new_user = UserModel(**(user.model_dump()))
    session.add(new_user)
    await session.commit()


@router.get('/')
async def get_users(session: SessionDep):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()


PaginationDep = Annotated[SPagination, Depends(SPagination)]


@router.get('/pages', response_model=list[SUserId])
async def get_users_pagination(
        session: SessionDep,
        pagination: PaginationDep
) -> list[SUserId]:
    query = (
        select(UserModel)
        .limit(pagination.limit)
        .offset(pagination.offset)
    )
    result = await session.execute(query)
    return result.scalars().all()
