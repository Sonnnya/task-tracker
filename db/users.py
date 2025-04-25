from sqlalchemy import select
from dependencies.common import PaginationDep, SessionDep
from repositories import UsersRepository
from models import OrmUser
from schemas.users import SUserAdd, SUser


class SQLAlchemyUsersRep(UsersRepository):
    model = OrmUser

    async def add_one(self, user: SUserAdd, session: SessionDep) -> int:
        new_user = self.model(**user)
        session.add(new_user)
        await session.commit()
        return new_user.id

    async def get_all(self, session: SessionDep) -> list[SUser]:
        query = select(self.model)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_paginated(
            self,
            session: SessionDep,
            pagination: PaginationDep,
    ) -> list[SUser]:
        query = (
            select(self.model)
            .limit(pagination.limit)
            .offset(pagination.offset)
        )
        result = await session.execute(query)
        return result.scalars().all()
