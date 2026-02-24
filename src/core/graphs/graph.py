from abc import ABC, abstractmethod
from typing import Any


class Graph(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def build(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def compile(self, *args, **kwargs) -> Any:
        raise NotImplementedError
    
    @abstractmethod
    def display(self, *args, **kwargs) -> Any:
        raise NotImplementedError
