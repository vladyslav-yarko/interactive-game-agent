# Test builder used for working with simple graph

from langgraph.graph import START, END

from src.core.builders.builder import Builder
from src.core.graphs.graph import Graph
from src.core.nodes.simple import (
    EntryNode,
    MoodRouterNode,
    GladNode,
    SadNode,
    PersonaNode
)
from src.core.constants.simple import SimpleNodeEnum


entry_node = EntryNode()
mood_router_node = MoodRouterNode()
glad_node = GladNode()
sad_node = SadNode()
persona_node = PersonaNode()


class SimpleBuilder(Builder):
    def __init__(self):
        self.entry_node = entry_node.node
        self.mood_router_node = mood_router_node.node
        self.sad_node = glad_node.node
        self.glad_node = sad_node.node
        self.persona_node = persona_node.node

    def build_graph(self, graph: Graph) -> None:
        graph.graph.add_node(SimpleNodeEnum.entry_node.value, self.entry_node)
        graph.graph.add_node(SimpleNodeEnum.glad_node.value, self.glad_node)
        graph.graph.add_node(SimpleNodeEnum.sad_node.value, self.sad_node)
        graph.graph.add_node(SimpleNodeEnum.persona_node.value, self.persona_node)

        graph.graph.add_edge(START, SimpleNodeEnum.entry_node.value)
        graph.graph.add_conditional_edges(
            SimpleNodeEnum.entry_node.value, 
            self.mood_router_node,
            {
                SimpleNodeEnum.glad_node.value: SimpleNodeEnum.glad_node.value,
                SimpleNodeEnum.sad_node.value: SimpleNodeEnum.sad_node.value
            }   
        )
        graph.graph.add_edge(SimpleNodeEnum.glad_node.value, SimpleNodeEnum.persona_node.value)
        graph.graph.add_edge(SimpleNodeEnum.sad_node.value, SimpleNodeEnum.persona_node.value)
        graph.graph.add_edge(SimpleNodeEnum.persona_node.value, END)
