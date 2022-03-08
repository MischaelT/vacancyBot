from abc import ABC, abstractmethod


class Base_db(ABC):
    def _validate(self, data):
        pass

    @abstractmethod
    def _write(self):
        pass

    @abstractmethod
    def _make_connection(self):
        pass

    @abstractmethod
    def _read(self):
        pass
