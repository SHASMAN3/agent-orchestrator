from abc import ABC, abstractmethod
from typing import List, Dict

class Memory(ABC):

    @abstractmethod
    def add_user(self, message: str):
        pass

    @abstractmethod
    def add_agent(self, message: str):
        pass

    @abstractmethod
    def get_history(self) -> List[Dict]:
        pass
