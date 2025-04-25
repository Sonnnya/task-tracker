from fastapi import APIRouter
from dependencies import PaginationDep, SessionDep
from schemas.users import SUserAdd, SUser, SPagination
from db import SQLAlchemyUsersRep


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def add_user(user: SUserAdd, session: SessionDep) -> int:
    new_user = user.model_dump()
    return await SQLAlchemyUsersRep().add_one(new_user, session)


@router.get('/', response_model=list[SUser])
async def get_users(session: SessionDep):
    return await SQLAlchemyUsersRep().get_all(session)


@router.get('/pages', response_model=list[SUser])
async def get_users_pagination(
        pagination: PaginationDep, session: SessionDep
) -> list[SUser]:
    return await SQLAlchemyUsersRep().get_paginated(session, pagination)
