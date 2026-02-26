import random

from src.core.nodes.node import Node
from src.core.constants.simple import SimpleNodeEnum
from src.core.schemas.simple import SimpleState


class EntryNode(Node):
    def __init__(self):
        pass
    
    def node(self, state: SimpleState) -> dict:
        return {
            "introduction": "is"
        }
