from abc import ABC, abstractmethod


class storage_Manager(ABC):
    def __validate(self):
        pass
    
    @abstractmethod
    def __write(self):
        pass

    @abstractmethod
    def __read(self):
        pass