from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    food_id = Column(Integer, ForeignKey("food.id"))

class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    grade = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))

    feedback = relationship("Feedback", back_populates="food")
    category = relationship("Category", back_populates="foods")

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    foods = relationship("Food", back_populates="category")
