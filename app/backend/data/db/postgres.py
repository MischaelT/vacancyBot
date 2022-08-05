import logging
from backend.models.vacancy import Vacancy

import psycopg2

from settings.config import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                             POSTGRES_PORT, POSTGRES_USER)


class Postgres_db():

    """
        Class provides access to postgres database
    """

    def __init__(self) -> None:

        super().__init__()

        self.__create_table_users()
        self.__create_table_vacancies()

    def get_user_by_id(self, params):
        query = """SELECT * FROM users WHERE ID='%s' """
        user_data = self._read(query, params)

        return user_data


    def update_user(self, params):

        query = '''UPDATE users
            SET area=%s, position=%s, exp=%s, lang=%s, city=%s, salary=%s
            WHERE id='%s'
        '''

        self._write(query=query, params=params)

    def create_user(self, params):

        query = '''INSERT INTO users (id, is_registered, area, position, exp, lang, city, salary)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                '''
        
        self._write(query=query, params=params)

    def clear_vacancy_table(self):

        query = '''TRUNCATE TABLE vacancies'''

        self._write(query)

    def get_vacancies_data(self, params: tuple) -> list:

        """
            Method returns data from database

        Returns:
            list(tuple): requested data
        """
        query = '''SELECT * FROM vacancies
                    WHERE exp=%s AND lang=%s AND area=%s AND position=%s;
                    '''
        return self._read(query, params)

    def push_vacancy_data(self, params: tuple) -> None:

        """
            Method pushes data to database
        """

        query = '''INSERT INTO vacancies (title, info, lang, area, position, exp, company_name, country, city, remote, salary, link, is_actual)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                '''
        self._write(query, params)

    def __create_table_users(self) -> None:

        """
            Method create table users.
            Raise Exception if table already exists
        """

        connection = self._make_connection()

        try:

            cursor = connection.cursor()

            create_users_query = '''CREATE TABLE IF NOT EXISTS users
                                (
                                ID              INT       PRIMARY KEY       NOT NULL,
                                IS_REGISTERED   BOOLEAN                     NOT NULL,
                                AREA            TEXT                        NOT NULL,
                                POSITION        TEXT                        NOT NULL,
                                EXP             TEXT                        NOT NULL,
                                LANG            TEXT                        NOT NULL,
                                CITY            TEXT                        NOT NULL,
                                SALARY          TEXT                        NOT NULL
                                ); '''

            cursor.execute(create_users_query)

            connection.commit()

            logging.info('Table users succesfully created')

        except (Exception) as exception:
            logging.exception(f'There was a problem during creating table users: {str(exception)}')

        finally:
            if connection:
                cursor.close()
                connection.close()

    def __create_table_vacancies(self) -> None:

        """
            Method create table vacancies.
            Raise Exception if table already exists
        """

        connection = self._make_connection()

        try:

            cursor = connection.cursor()

            create_vacancies_query = '''CREATE TABLE IF NOT EXISTS vacancies
                                (
                                ID             SMALLSERIAL   PRIMARY KEY    NOT NULL,
                                TITLE          TEXT                         NOT NULL,
                                INFO           TEXT                         NOT NULL,                                
                                LANG           TEXT                                 ,
                                AREA           TEXT                         NOT NULL,
                                POSITION       TEXT                         NOT NULL,
                                EXP            TEXT                         NOT NULL,
                                COMPANY_NAME   TEXT                                 ,
                                COUNTRY        TEXT                         NOT NULL,                                
                                CITY           TEXT                         NOT NULL,
                                REMOTE         TEXT                                 ,
                                SALARY         SMALLINT                             ,
                                LINK           TEXT                         NOT NULL,
                                IS_ACTUAL      BOOL                         NOT NULL
                                ); '''

            cursor.execute(create_vacancies_query)

            connection.commit()

            logging.info('Table vacancies succesfully created')

        except (Exception) as exception:
            logging.exception(f'There was a problem during creating table vacancies: {str(exception)}')

        finally:
            if connection:
                cursor.close()
                connection.close()

    def _make_connection(self):

        """
            Method connecting to database using autentication data from config.py

        Returns:
           connection: Connection object
        """

        try:
            connection = psycopg2.connect(
                                        user=POSTGRES_USER,
                                        password=POSTGRES_PASSWORD,
                                        host=POSTGRES_HOST,
                                        port=POSTGRES_PORT,
                                        database=POSTGRES_DB
                                        )

        except (Exception) as exception:
            logging.exception(f'There was a problem during creating connection: {str(exception)}')

        return connection

    def _write(self, query: str, params: tuple = ()) -> None:

        """
        Method writes data to database.

        Args:
            query (str): SQL query
            params (tuple): parameters for inserting to query
        """

        connection = self._make_connection()

        try:

            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()

        except Exception as exception:
            logging.exception(f'There was a problem during writing: {str(exception)}')

        finally:
            if connection:
                cursor.close()
                connection.close()

    def _read(self, query: str, params: tuple) -> list:

        """
            Method receives data from database

        Returns:
            list: requested data
        """

        connection = self._make_connection()

        record = []

        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            record = cursor.fetchall()

        except Exception as exception:
            logging.exception(f'There was a problem during reading: {str(exception)}')

        finally:
            if connection:
                cursor.close()
                connection.close()

        return record
