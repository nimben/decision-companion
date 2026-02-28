from pydantic import BaseModel, Field
from typing import List


class Book(BaseModel):
    name: str
    pages: int = Field(gt=0)
    complexity: int = Field(ge=1, le=5)
    emotional_intensity: int = Field(ge=1, le=5)
    learning_depth: int = Field(ge=1, le=5)


class Weights(BaseModel):
    cognitive: float = Field(ge=0)
    time: float = Field(ge=0)
    learning: float = Field(ge=0)
    emotion: float = Field(ge=0)


class EvaluationRequest(BaseModel):
    books: List[Book]
    available_hours: float = Field(gt=0)
    reading_speed: float = Field(gt=0, default=40)
    weights: Weights