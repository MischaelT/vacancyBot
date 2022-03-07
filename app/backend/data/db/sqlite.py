import sqlite3
from sqlite3.dbapi2 import Error

from backend.data.db.base_db import Base_db


class Db_manager(Base_db):

    def __init__(self) -> None:
        super().__init__()

    def get_data(self, query) -> list:
        return self._read(query)

    def push_data(self, data):
        self._validate(data)
        self._write(data)

    def _make_connection(self):
        try:
            con = sqlite3.connect('vacancies.db')
        except Error:
            pass

        return con

    def _write(self, query):

        con = self._make_connection()

        cur = con.cursor()

        cur.execute(query)

        con.commit()

        con.close()

    def _read(self, query):

        con = self._make_connection()

        cur = con.cursor()

        cur.execute(query)

        data = cur.fetchall()

        return data
