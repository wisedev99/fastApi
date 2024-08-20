from pydantic import BaseModel
from typing import List, Optional

class Feedback(BaseModel):
    comment: str

class Food(BaseModel):
    id: int
    name: str
    grade: str
    feedback: List[Feedback] = []

class Category(BaseModel):
    id: int
    name: str
    # foods: List[Food] = []

class CategoryCreate(BaseModel):
    name: str

class FeedbackCreate(BaseModel):
    comment: str
