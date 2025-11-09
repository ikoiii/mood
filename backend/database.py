from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database configuration - Using MySQL/XAMPP
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/mood_tracker")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True  # Enable SQL logging for debugging
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()