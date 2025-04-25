from abc import ABC, abstractmethod


class UsersRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError
