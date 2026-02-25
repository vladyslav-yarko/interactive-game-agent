# Test agent used for working with simple graph


from src.core.agents.local import LocalAgent
from src.core.graphs.simple import simple_graph
from src.core.schemas.simple import SimpleStateInput, SimpleStateOutput


class SimpleAgent(LocalAgent):
    def __init__(self):
        super().__init__(
            graph=simple_graph
        )
    
    async def run(self, input: SimpleStateInput) -> SimpleStateOutput:
        result = await super().run(
            input=input
        )
        return result


simple_agent = LocalAgent(
    graph=simple_graph
)
