from src.core.agents.agent import Agent
from src.core.graphs import Graph


class LocalAgent(Agent):
    def __init__(self, graph: Graph):
        self.graph = graph

    def __getattr__(self, item):
        return getattr(self.graph, item)
