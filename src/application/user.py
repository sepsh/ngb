from sqlalchemy import Engine, create_engine
from sqlmodel import Session, select

from src.application.dto import UserBalanceDTO, UserDTO
from src.data.models import User


class UserService:
    engine: Engine

    def __init__(self):
        self.engine = self.__create_engine()

    def create_user(self, user: UserDTO) -> None:
        user_entity = User(username=user.username, nickname=user.nickname)
        with Session(self.engine) as session:
            session.add(user_entity)
            session.commit()

    def get_balance(self, username: str) -> UserBalanceDTO | None:
        with Session(self.engine) as session:
            statement = select(User).where(User.username == username)
            user_entity = session.exec(statement=statement).first()
            return UserBalanceDTO(amount=user_entity.balance) if user_entity else None

    @staticmethod
    def __create_engine():
        sqlite_file_name = "database.db"
        sqlite_url = f"sqlite:///{sqlite_file_name}"

        connect_args = {"check_same_thread": False}
        return create_engine(sqlite_url, echo=True, connect_args=connect_args)
