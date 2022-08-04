from abc import ABC, abstractmethod

from pathlib import Path

class BaseSource(ABC):

    def __init__(self) -> None:

        self.headers = {'User-Agent': ''}
        self.proxy = {'http': 'http//:'}

        proxies_path = Path(__file__).parent / "../parser/proxies.txt"

        with proxies_path.open('proxies.txt', 'r') as f:
            self.proxies_list = f.read().split('\n')

        agents_path = Path(__file__).parent / "../parser/user-agents.csv"

        with agents_path.open('user-agents.txt', 'r') as f:
            self.user_agents_list = f.read().split('\n')

        self.parsed_data = []

        super().__init__()

    @abstractmethod
    def parse_content(self):
        pass

    @abstractmethod
    def make_futures(self):
        pass