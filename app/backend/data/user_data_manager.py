from backend.data.db.postgres import Postgres_db
from backend.models.user import User


class User_data_manager():

    """
        Class provides methods for interactions with user data
    """    

    def __init__(self, db: Postgres_db) -> None:
        self.db = db

    def get_user(self, user_id: int) -> User:

        """
            Method returms user from database

        Args:
            user_id (int): user telegram id

        Returns:
            User: user model
        """

        return self.__get_user_by_id(user_id=user_id)

    def set_user(self, user: User) -> None:

        """
        Public method that sets user

        Args:
            user (User): user model
        """

        return self.__set_user(user=user)

    def __set_user(self, user: User) -> None:

        """
        Private method that pushes user settings to database.
        Based on that user is registered or not

        Args:
            user (User): user model
        """        

        if user.is_registered:

            params = (user.experience, user.language, user.city, user.salary, user.user_id)

            query = '''UPDATE users 
                        SET exp =%s,lang=%s, city=%s, salary=%s
                        WHERE id='%s'
                 '''
        else:

            params = (user.user_id, user.is_registered, user.experience, user.language, user.city, user.salary)

            query = '''INSERT INTO users (id, is_registered, exp, lang, city, salary)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    '''

        self.db.push_data(query, params)

    def __get_user_by_id(self, user_id: int) -> User:

        """
        Method find user in database by id.
        If user exists it returns completely filled user model,
        if not - new user model with is_registered = False

        Args:
            user_id (int): telegram user id

        Returns:
            User: user model
        """

        params = (user_id,)
        query = """SELECT * FROM users WHERE ID='%s' """

        user_data = self.db.get_data(query, params=params)

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
