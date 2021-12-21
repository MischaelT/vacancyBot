import sqlite3

from backend.data.storage.storage_manager import storage_Manager


class Db_manager(storage_Manager):

    def get_data(self) -> list:
        pass

    def push_data(self, data):
        self._validate(data)
        self._write(data)

    def _write(self, data):
        con = sqlite3.connect('vacancies.db')
        cur = con.cursor()

        data_to_db = []

        for value in data.values():
            data_to_db.append(value)

        cur.execute("INSERT INTO Vacancies(title, city, info, link, remote) VALUES (?,?,?,?,?)", data_to_db)

        con.commit()

        con.close()

    def _read(self, data):
        pass
