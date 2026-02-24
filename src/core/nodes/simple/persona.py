from src.core.nodes.node import Node
from src.core.schemas.simple import SimpleState


class PersonaNode(Node):
    def __init__(self):
        pass
    
    def node(self, state: SimpleState) -> dict:
        return {
            "persona": f"{state.name} is {state.mood}"
        }
