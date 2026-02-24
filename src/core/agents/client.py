from langgraph_sdk import get_client

from src.core.agents.agent import Agent


class ClientAgent(Agent):
    def __init__(self, url: str, graph_name: str):
        self.client = get_client(
            url=url
        )
        self.graph_name = graph_name

    def __getattr__(self, item):
        return getattr(self.client, item)
