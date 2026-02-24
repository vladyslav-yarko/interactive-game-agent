from typing import Optional, Type

from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph
from pydantic import BaseModel
from IPython.display import Image, display, DisplayHandle

from src.core.graphs.graph import Graph
from src.core.builders import Builder


class BaseGraph(Graph):
    def __init__(
        self,
        overall_state: Type[BaseModel],
        input_state: Type[BaseModel],
        output_state: Type[BaseModel]
    ):
        self.__overall_state = overall_state
        self.__input_state = input_state
        self.__output_state = output_state
        self.__graph = StateGraph(
            self.__overall_state,
            input_schema=self.__input_state,
            output_schema=self.__output_state
        )
        self.__compiled_graph: CompiledStateGraph

    def build(self, builder: Builder) -> None:
        builder.build_graph(self)
    
    def compile(self) -> CompiledStateGraph:
        graph = self.__graph.compile()
        return graph

    def display(self) -> Optional[DisplayHandle]:
        if self.__compiled_graph is not None:
            image = display(Image(self.__compiled_graph.get_graph().draw_mermaid_png()))
        else:
            image = None
        return image

    @property
    def graph(self) -> StateGraph:
        return self.__graph
    
    @property
    def compiled_graph(self) -> Optional[CompiledStateGraph]:
        return self.__compiled_graph
