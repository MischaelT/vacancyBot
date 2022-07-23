from abc import ABC, abstractmethod

class BaseSource(ABC):

    def __init__(self) -> None:

        self.headers = {'User-Agent': ''}
        self.proxy = {'http': 'http//:'}

        with open('proxies.txt', 'r') as f:
            self.proxies_list = f.read().split('\n')

        with open('user-agents.txt', 'r') as f:
            self.user_agents_list = f.read().split('\n')

        self.parsed_data = []

        super().__init__()

    @abstractmethod
    def parse_content(self):
        pass

    @abstractmethod
    def make_futures(self):
        pass