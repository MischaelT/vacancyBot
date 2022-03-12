import csv
import logging

from backend.data.view.view_manager import view_Manager


class Csv_manager(view_Manager):

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
        except IOError as exception:
            logging.exception(f'There was a problem during writing to csv: {str(exception)}')

    def _read(self):
        pass
