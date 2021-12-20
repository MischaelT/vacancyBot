from app.backend.data.storage.db_manager import Db_manager

class Vacancy_filter():
    def __init__(self) -> None:
        self.db = Db_manager()