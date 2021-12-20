from app.backend.data.storage.db_manager import Db_manager

class User_data_manager():
    def __init__(self) -> None:
        self.db = Db_manager()