from abc import ABC, abstractmethod


class Base_db(ABC):
    def _validate(self, data):
        for value in data.values():
            value = " ".join(value.split())

    @abstractmethod
    def _write(self):
        pass

    @abstractmethod
    def _make_connection(self):
        pass

    @abstractmethod
    def _read(self):
        pass
