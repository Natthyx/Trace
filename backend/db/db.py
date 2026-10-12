from sqlmodel import Session, SQLModel, create_engine
from core.config import settings

DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session