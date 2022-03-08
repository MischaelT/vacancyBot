from backend.data.db.postgres import Db_manager
from backend.models.user import User


class User_data_manager():

    def __init__(self, manager: Db_manager) -> None:
        self.db = manager

    def get_user(self, user_id) -> User:
        return self.__get_user_by_id(user_id=user_id)

    def set_user(self, user: User) -> None:
        return self.__set_user(user=user)

    def __set_user(self, user: User) -> None:
        query = f'''INSERT INTO users (id, is_registered, exp, lang, city, salary)
                    VALUES ('{user.user_id}', '{user.is_registered}', '{user.experience}', '{user.language}', '{user.city}', '{user.salary}')
                 '''
        self.db.push_data(query)

    def __get_user_by_id(self, user_id: int) -> User:

        query = f'''SELECT * FROM users WHERE ID = {user_id}'''

        try:
            user_data = self.db.get_data(query)
        except (Exception) as exception:
            print('НЕт юзера', exception)

        if len(user_data) == 0:

            user = User(
                        user_id=user_id,
                        is_registered=False,
                        experience='',
                        language='',
                        city='',
                        salary=''
                        )
        else:
            user_data=user_data[0]
            user = User(
                        user_id=user_id,
                        is_registered=True,
                        experience=user_data[2],
                        language=user_data[3],
                        city=user_data[4],
                        salary=user_data[5]
                        )


        return user
