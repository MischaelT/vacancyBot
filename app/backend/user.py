from app.backend.data.storage.db_manager import DataManager

class User():
    def __init__(self) -> None:
        self.data_manager = DataManager()
