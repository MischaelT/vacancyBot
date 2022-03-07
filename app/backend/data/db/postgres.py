from backend.data.db.base_db import Base_db

import psycopg2

from settings.config import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                             POSTGRES_PORT, POSTGRES_USER)


class Db_manager(Base_db):

    def __init__(self) -> None:

        super().__init__()

        self.user = POSTGRES_USER
        self.password = POSTGRES_PASSWORD
        self.host = POSTGRES_HOST
        self.port = POSTGRES_PORT
        self.db = POSTGRES_DB

    def create_table(self):

        try:
            connection = self.__make_connection()

            cursor = connection.cursor()

            create_users_query = '''CREATE TABLE users
                                (
                                ID INT PRIMARY KEY     NOT NULL,
                                EXP            TEXT    NOT NULL,
                                LANG           TEXT,
                                CITY           TEXT
                                ); '''

            cursor.execute(create_users_query)

            create_vacancies_query = '''CREATE TABLE vacancies
                                (
                                ID INT PRIMARY KEY      NOT NULL,
                                DATE           DATE     NOT NULL,
                                EXP            TEXT     NOT NULL,
                                LANG           TEXT     NOT NULL,
                                CITY           TEXT,
                                TITLE          TEXT,
                                INFO           TEXT,
                                LINK           TEXT
                                ); '''

            cursor.execute(create_vacancies_query)

            connection.commit()

        except (Exception):
            pass
        finally:
            if connection:
                cursor.close()
                connection.close()

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

        try:
            connection = self._make_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

        except Exception:
            pass

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
