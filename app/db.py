from sqlmodel import Session, create_engine
from .models import Base

db_url = f"sqlite:///../app.db"  # SQLite database URL

engine = create_engine(db_url)

def create_db_and_tables():
    Base.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session