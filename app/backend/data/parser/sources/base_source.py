from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from app.backend.models.vacancy import Vacancy


class BaseSource(ABC):

    def __init__(self) -> None:

        proxies_path = Path(__file__).parent.parent / "../parser/proxies.txt"

        with proxies_path.open() as f:
            self.proxies_list = f.read().split('\n')

        agents_path = Path(__file__).parent.parent / "../parser/user-agents.txt"

        with agents_path.open() as f:
            self.user_agents_list = f.read().split('\n')

        self.parsed_data: List[Vacancy] = []

        super().__init__()

    @abstractmethod
    def make_futures(self):
        pass
