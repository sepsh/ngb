from sqlalchemy import Engine, create_engine
from sqlmodel import Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine: Engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)
