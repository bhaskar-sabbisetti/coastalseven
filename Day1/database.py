from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



DATABASE_URL = "postgresql://postgres:Bhaskar_6281@localhost:5432/test_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
