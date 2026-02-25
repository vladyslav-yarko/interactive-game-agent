# Test schemas used for simple graph

from typing import Optional

from pydantic import BaseModel, Field


class SimpleState(BaseModel):
    name: str
    mood: Optional[str] = Field(None)
    persona: Optional[str] = Field(None)
    
    
class SimpleStateInput(BaseModel):
    name: str
    
    
class SimpleStateOutput(BaseModel):
    persona: str
