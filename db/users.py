from repositories import UsersReposetory


class SQLAlchemyUsersRepository(UsersReposetory):
    model = None

    @classmethod
    def get_one():
        raise NotImplementedError

    @classmethod
    def get_all():
        raise NotImplementedError
