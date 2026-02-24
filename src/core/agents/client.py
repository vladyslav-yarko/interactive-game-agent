from langgraph_sdk import get_client

from src.core.agents.agent import Agent


class ClientAgent(Agent):
    def __init__(self, url: str, graph_name: str):
        self.__client = get_client(
            url=url
        )
        self.__graph_name = graph_name

    async def run(self, input: BaseModel) -> BaseModel:
        result = self.__client.runs.create(
            assistant_id=self.__graph_name
        )
        return result

    async def stream(self, input: BaseModel) -> Iterator[str]:
        pass
