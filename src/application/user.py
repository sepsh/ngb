from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.application.dto import UserBalanceDTO, UserDTO
from src.data.models import User, Base


class UserService:
    def __init__(self, db_url: str = "sqlite:///database.db"):
        self.engine = create_engine(db_url, echo=True, connect_args={"check_same_thread": False})
        Base.metadata.create_all(self.engine)  # Ensure tables are created

    def get_user(self, username: str) -> UserDTO | None:
        with Session(self.engine) as session:
            statement = select(User).where(User.username == username)
            user = session.scalars(statement).first()
            return UserDTO(username=user.username, nickname=user.nickname, balance=user.balance) if user else None

    def list_users(self) -> list[UserDTO]:
        with Session(self.engine) as session:
            statement = select(User)
            users = session.scalars(statement).all()
            return [UserDTO(username=u.username, nickname=u.nickname, balance=u.balance) for u in users]

    def create_user(self, user: UserDTO) -> None:
        user_entity = User(username=user.username, nickname=user.nickname)
        with Session(self.engine) as session:
            session.add(user_entity)
            session.commit()

    def get_balance(self, username: str) -> UserBalanceDTO | None:
        with Session(self.engine) as session:
            statement = select(User).where(User.username == username)
            user = session.scalars(statement).first()
            return UserBalanceDTO(amount=user.balance) if user else None
