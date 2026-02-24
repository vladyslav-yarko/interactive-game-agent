from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph
from pydantic import BaseModel

from src.core.graphs.graph import Graph
from src.core.builders import Builder


class BaseGraph(Graph):
    def __init__(
        self,
        overall_state: BaseModel,
        input_state: BaseModel,
        output_state: BaseModel
    ):
        self.overall_state = overall_state
        self.input_state = input_state
        self.output_state = output_state
        self.graph = StateGraph(
            self.overall_state,
            input_schema=self.input_state,
            output_schema=self.output_state
        )

    def build(self, builder: Builder) -> None:
        builder.build_graph(self.graph)
    
    def compile(self) -> CompiledStateGraph:
        graph = self.graph.compile()
        return graph
