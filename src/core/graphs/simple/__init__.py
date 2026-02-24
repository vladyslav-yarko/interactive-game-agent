# Test graph used for working with simple graph


from src.core.graphs.base import BaseGraph
from src.core.schemas.simple import (
    SimpleState,
    SimpleStateInput,
    SimpleStateOutput
)


simple_graph = BaseGraph(
    overall_state=SimpleState,
    input_state=SimpleStateInput,
    output_state=SimpleStateOutput
)


