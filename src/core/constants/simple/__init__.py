import enum


class SimpleNodeEnum(str, enum.Enum):
    entry_node = "entry_node"
    sad_node = "sad_node"
    glad_node = "glad_node"
    persona_node = "persona_node"
