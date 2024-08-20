from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from crud import get_categories, create_category, create_feedback, get_foods
from schemas import CategoryCreate, FeedbackCreate, Category,Feedback,Food

app = FastAPI()

# Initialize database
init_db()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Online Menu API! 🌟"}

@app.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = get_categories(db, skip=skip, limit=limit)
    return categories

# @app.post("/categories/", response_model=Category)
# def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
#     return create_category(db=db, category=category)

# @app.get("/categories/{category_id}/foods/", response_model=list[Food])
# def read_foods(category_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return get_foods(db=db, category_id=category_id, skip=skip, limit=limit)

# @app.post("/foods/{food_id}/feedback/", response_model=Feedback)
# def create_new_feedback(food_id: int, feedback: FeedbackCreate, db: Session = Depends(get_db)):
#     return create_feedback(db=db, feedback=feedback, food_id=food_id)
