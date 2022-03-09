from backend.data.db.base_db import Base_db

import psycopg2

# from settings.config import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
#                              POSTGRES_PORT, POSTGRES_USER)


class Db_manager(Base_db):

    def __init__(self) -> None:

        super().__init__()

        self.user = 'user'
        self.password = 'password'
        self.host = 'localhost'
        self.port = '5432'
        self.db = 'db'

        self.create_table()

    def create_table(self):

        try:
            connection = self._make_connection()

            cursor = connection.cursor()

            create_users_query = '''CREATE TABLE users
                                (
                                ID              INT       PRIMARY KEY       NOT NULL,
                                IS_REGISTERED   BOOLEAN                     NOT NULL,                                
                                EXP             TEXT                        NOT NULL,
                                LANG            TEXT                        NOT NULL,
                                CITY            TEXT                        NOT NULL,
                                SALARY          TEXT                        NOT NULL
                                ); '''

            cursor.execute(create_users_query)

            create_vacancies_query = '''CREATE TABLE vacancies
                                (
                                ID             SMALLSERIAL                  NOT NULL,
                                DATE           DATE                         NOT NULL,
                                EXP            TEXT                         NOT NULL,
                                LANG           TEXT                         NOT NULL,
                                CITY           TEXT                         NOT NULL,
                                TITLE          TEXT                         NOT NULL,
                                INFO           TEXT                         NOT NULL,
                                LINK           TEXT                         NOT NULL,
                                SALARY         SMALLINT                     NOT NULL
                                ); '''

            cursor.execute(create_vacancies_query)

            connection.commit()
            print('успешно')

        except (Exception) as exception:
            print('не успешно', exception)
            
        # finally:
        #     if connection:
        #         cursor.close()
        #         connection.close()

    def get_data(self, request_text) -> list:
        return self._read(request_text)

    def push_data(self, data):
        self._validate(data)
        self._write(data)

    def _make_connection(self):
        try:
            connection = psycopg2.connect(
                                        user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port,
                                        database=self.db
                                        )

        except (Exception):
            pass

        return connection

    def _write(self, query):

        connection = self._make_connection()

        try:

            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

        except Exception as ex:
            print(ex)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def _read(self, query):

        try:
            connection = self._make_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()

        except Exception:
            pass

        finally:
            if connection:
                cursor.close()
                connection.close()

        return record
