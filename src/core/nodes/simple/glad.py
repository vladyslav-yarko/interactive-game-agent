from src.core.nodes.node import Node
from src.core.schemas.simple import SimpleState


class GladNode(Node):
    def __init__(self):
        pass
    
    def node(self, state: SimpleState) -> dict:
        return {
            "mood": "glad"
        }
