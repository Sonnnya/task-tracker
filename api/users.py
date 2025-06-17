from fastapi import APIRouter
from dependencies import PaginationDep, SessionDep
from schemas.users import SUserAdd, SUser, SPagination
from dependencies import UsersServiceDep


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def add_user(user: SUserAdd, session: SessionDep, user_service: UsersServiceDep) -> int:
    new_user = user.model_dump()
    return await user_service.add_one(session, new_user)


@router.get('/', response_model=list[SUser])
async def get_users(session: SessionDep, user_service: UsersServiceDep):
    return await user_service.get_all(session)


@router.get('/pages', response_model=list[SUser])
async def get_users_pagination(
        pagination: PaginationDep, session: SessionDep, user_service: UsersServiceDep
) -> list[SUser]:
    return await user_service.get_paginated(session, pagination)
