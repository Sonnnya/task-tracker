from abc import ABC, abstractmethod


class TasksRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError
