from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

#NOTE: node is extraordinary core component. Builder will be specifically inherited for specific purpose

class Node(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def node(self, *args, **kwargs) -> BaseModel:
        raise NotImplementedError
