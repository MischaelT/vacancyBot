from backend.data.storage.db_manager import Db_manager


class User():
    def __init__(self) -> None:
        self.data_manager = Db_manager()
