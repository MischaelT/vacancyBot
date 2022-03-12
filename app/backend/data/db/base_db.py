from abc import ABC, abstractmethod


class Base_db(ABC):

    """
        Base class for all databases
    """

    def _validate(self):
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
