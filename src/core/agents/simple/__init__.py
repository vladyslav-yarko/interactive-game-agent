# Test agent used for working with simple graph


from src.core.agents.local import LocalAgent
from src.core.graphs.simple import simple_graph


simple_agent = LocalAgent(
    graph=simple_graph
)
