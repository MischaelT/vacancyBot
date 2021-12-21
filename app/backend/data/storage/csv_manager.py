import csv

from backend.data.storage.storage_manager import storage_Manager


class Csv_manager(storage_Manager):

    def push_data(self, data):
        self._validate(data)
        self._write(data)

    def _write(self, data):
        try:
            with open('vacancies.csv', 'a') as file:
                writer = csv.writer(file)
                data_to_csv = []
                for element in data.values():
                    data_to_csv.append(element)
                writer.writerow(data_to_csv)
        except IOError:
            print("I/O error")  # noqa

    def _read(self):
        pass
