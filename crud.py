from sqlalchemy.orm import Session
from models import Category, Food, Feedback
from schemas import CategoryCreate, FeedbackCreate

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def get_foods(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(Food).filter(Food.category_id == category_id).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_feedback(db: Session, feedback: FeedbackCreate, food_id: int):
    db_feedback = Feedback(comment=feedback.comment, food_id=food_id)
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback
