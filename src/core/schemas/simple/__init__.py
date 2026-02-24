# Test schemas used for simple graph


from pydantic import BaseModel


class SimpleState(BaseModel):
    name: str
    mood: str
    persona: str
    
    
class SimpleStateInput(BaseModel):
    name: str
    
    
class SimpleStateOutput(BaseModel):
    persona: str
