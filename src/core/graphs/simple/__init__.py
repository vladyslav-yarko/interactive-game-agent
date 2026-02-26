# Test graph used for working with simple graph


from src.core.graphs.base import BaseGraph
from src.core.schemas.simple import (
    SimpleState,
    SimpleStateInput,
    SimpleStateOutput
)
from src.core.builders.simple import SimpleBuilder

simple_graph_builder= SimpleBuilder()

simple_graph = BaseGraph(
    overall_state=SimpleState,
    input_state=SimpleStateInput,
    output_state=SimpleStateOutput
)
simple_graph.build(simple_graph_builder)
simple_graph.compile()
