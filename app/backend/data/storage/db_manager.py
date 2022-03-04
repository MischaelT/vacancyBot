import sqlite3
from sqlite3.dbapi2 import Error

from backend.data.storage.storage_manager import storage_Manager


class Db_manager(storage_Manager):

    def __init__(self) -> None:
        super().__init__()

    def get_data(self, id) -> list:
        return self._read(id)

    def push_data(self, data):
        self._validate(data)
        self._write(data)

    def _write(self, data):

        try:
            con = sqlite3.connect('vacancies.db')
        except Error:
            pass

        cur = con.cursor()  

        data_to_db = []

        for value in data.values():
            data_to_db.append(value)

        cur.execute("INSERT INTO Vacancies(title, city, info, link, remote) VALUES (?,?,?,?,?)", data_to_db)

        con.commit()

        con.close()

    def _read(self, id):

        try:
            con = sqlite3.connect('vacancies.db')
        except Error:
            pass

        cur = con.cursor()

        cur.execute("SELECT * FROM Vacancies WHERE id=?", (id+3650,))

        data = cur.fetchall()

        return data

    def validate_to_read(self,data):
        pass
