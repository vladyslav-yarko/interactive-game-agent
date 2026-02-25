import random

from src.core.nodes.node import Node
from src.core.constants.simple import SimpleNodeEnum
from src.core.schemas.simple import SimpleState


class MoodRouterNode(Node):
    def __init__(self):
        pass
    
    def node(self, state: SimpleState) -> str:
        if random.random() < 0.5:
            return SimpleNodeEnum.sad_node.value
        return SimpleNodeEnum.glad_node.value
