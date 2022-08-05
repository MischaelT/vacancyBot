from abc import ABC, abstractmethod

from pathlib import Path

class BaseSource(ABC):

    def __init__(self) -> None:

        proxies_path = Path(__file__).parent.parent / "../parser/proxies.txt"

        with proxies_path.open() as f:
            self.proxies_list = f.read().split('\n')

        agents_path = Path(__file__).parent.parent / "../parser/user-agents.txt"

        with agents_path.open() as f:
            self.user_agents_list = f.read().split('\n')

        self.parsed_data = []

        super().__init__()

    @abstractmethod
    def make_futures(self):
        pass
