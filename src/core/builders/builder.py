from abc import ABC, abstractmethod
from src.core.graph import Graph


#NOTE: builder is extraordinary core component. Builder will be specifically inherited for specific purpose

class Builder(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def build_graph(self, graph: Graph) -> None:
        raise NotImplementedError
