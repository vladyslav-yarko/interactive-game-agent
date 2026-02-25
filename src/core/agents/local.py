from typing import Iterator

from pydantic import BaseModel

from src.core.agents.agent import Agent
from src.core.graphs import Graph


class LocalAgent(Agent):
    def __init__(self, graph: Graph):
        self.__graph = graph

    async def run(self, input: BaseModel):
        result = await self.__graph.compiled_graph.ainvoke(input)
        return result

    async def stream(self, input: BaseModel) -> Iterator[str]:
        pass
