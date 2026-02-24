from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError
