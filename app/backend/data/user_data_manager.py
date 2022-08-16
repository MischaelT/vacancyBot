import logging
from typing import List

from backend.data.db.postgres import PostgresDB
from backend.models.user import User


class UserDataManager():

    """
        Class provides methods for interactions with user data
    """

    def __init__(self, db: PostgresDB) -> None:
        self.db = db

    def get_user(self, user_id: int) -> User:

        """
            Method returms user from database

        Args:
            user_id (int): user telegram id

        Returns:
            User: user model
        """

        params = (user_id,)

        user_data = self.db.get_user_by_id(params=params)

        if len(user_data) == 0:

            user_data = [user_id, False, '', '', '', '', '', '']

            user = self.__create_user(data=user_data)

        else:
            user_data = list(user_data[0])
            user_data[0] = user_id
            user_data[1] = True

            user = self.__create_user(data=user_data)

        return user

    def set_user(self, user: User) -> None:

        """
        Public method that sets user

        Args:
            user (User): user model
        """

        if user.is_registered:

            params = (user.area,
                      user.position,
                      user.experience,
                      user.language,
                      user.location,
                      user.salary,
                      user._id)

            self.db.update_user(params=params)

        else:
            user.is_registered = True
            params = (user._id,
                      user.is_registered,
                      user.area,
                      user.position,
                      user.experience,
                      user.language,
                      user.location,
                      user.salary)

            self.db.create_user(params)

    def get_users(self) -> List[User]:

        """
            Method returms user from database

        Args:
            user_id (int): user telegram id

        Returns:
            User: user model
        """

        users_data = self.db.get_all_users()

        logging.debug(users_data)

        users = []

        for user_data in users_data:
            logging.debug(user_data)
            user = self.__create_user(user_data)
            users.append(user)

        return users

    def __create_user(self, data: list) -> User:

        user = User(_id=data[0],
                    is_registered=data[1],
                    area=data[2],
                    position=data[3],
                    experience=data[4],
                    language=data[5],
                    location=data[6],
                    salary=data[7])
        return user
