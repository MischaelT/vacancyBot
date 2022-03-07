from backend.models.user import User


class User_data_manager():

    def __init__(self, manager) -> None:
        self.db = manager

    def get_user(self, user_id) -> User:
        return self.__get_user_by_id(user_id=user_id)

    def __get_user_by_id(self, user_id) -> User:

        query = f'''SELECT * FROM users WHERE ID = {user_id}'''
        self.db.get_data(query)

        # TODO получение данных из БД и создание объекта USER

        user = User('', '', '', '')

        return user
