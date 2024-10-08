import os
import sqlalchemy as sqlalchemy_package

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variable
DATABASE_URL = "sqlite:///./sqlite.db"

# Create the SQLAlchemy engine
engine = sqlalchemy_package.create_engine(DATABASE_URL,connect_args={"check_same_thread": True})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
