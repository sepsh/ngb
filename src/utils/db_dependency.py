from sqlalchemy.orm.session import Session
from src.config.database import SessionLocal


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session

    finally:
        session.close()
