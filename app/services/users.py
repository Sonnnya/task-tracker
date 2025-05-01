from dependencies.common import PaginationDep, SessionDep
from repositories.users import UsersRepository
from schemas.users import SUser, SUserAdd


class UsersService():
    def __init__(self, user_repo: UsersRepository):
        self.repo = user_repo()

    async def add_one(self, session: SessionDep, user: SUserAdd) -> list[SUser]:
        return await self.repo.add_one(session, user)

    async def get_all(self, session: SessionDep):
        return await self.repo.get_all(session)

    async def get_paginated(self, session: SessionDep, pagination: PaginationDep):
        return await self.repo.get_paginated(session, pagination)
