from abc import ABC, abstractmethod


class UsersReposetory(ABC):
    @abstractmethod
    def get_one():
        raise NotImplementedError

    @abstractmethod
    def get_all():
        raise NotImplementedError
