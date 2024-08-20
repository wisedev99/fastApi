from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

# Define Base
Base = declarative_base()

# Define your models
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="foods")

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey('foods.id'))
    comments = Column(String)
    grade = Column(Integer)

    food = relationship("Food", back_populates="feedbacks")

# Establish relationships
Category.foods = relationship("Food", back_populates="category")
Food.feedbacks = relationship("Feedback", back_populates="food")

# Database setup
DATABASE_URL = "postgresql://wisedev99:i5irXx3SqzcgeLyf2TnWj3eCRzfRf1YS@dpg-cr1rkhogph6c73bbop7g-a.oregon-postgres.render.com/menu_p3g2"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    # Insert sample data
    with SessionLocal() as session:
        # Create sample categories
        category1 = Category(name='Appetizers')
        category2 = Category(name='Main Courses')
        category3 = Category(name='Desserts')

        session.add(category1)
        session.add(category2)
        session.add(category3)
        session.commit()

        # Create sample foods
        food1 = Food(name='Spring Rolls', category_id=category1.id)
        food2 = Food(name='Grilled Salmon', category_id=category2.id)
        food3 = Food(name='Chocolate Cake', category_id=category3.id)

        session.add(food1)
        session.add(food2)
        session.add(food3)
        session.commit()

        # Create sample feedback
        feedback1 = Feedback(food_id=food1.id, comments='Delicious!', grade=5)
        feedback2 = Feedback(food_id=food2.id, comments='Too salty.', grade=3)
        feedback3 = Feedback(food_id=food3.id, comments='Heavenly!', grade=5)

        session.add(feedback1)
        session.add(feedback2)
        session.add(feedback3)
        session.commit()

if __name__ == "__main__":
    init_db()
