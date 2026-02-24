from abc import ABC, abstractmethod
from typing import Iterator


class Agent(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    # graph invocation
    @abstractmethod
    async def run(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def stream(self) -> Iterator[str]:
        raise NotImplementedError
