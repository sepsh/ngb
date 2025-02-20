from sqlalchemy import Engine
from sqlmodel import Session, create_engine, select, func, update

from src.application.dto import TransactionDTO
from src.data.models import Transaction, TransactionType, User


class TransactionService:
    engine: Engine

    def __init__(self):
        self.engine = self.__create_engine()

    @staticmethod
    def __create_engine():
        sqlite_file_name = "database.db"
        sqlite_url = f"sqlite:///{sqlite_file_name}"

        connect_args = {"check_same_thread": False}
        return create_engine(sqlite_url, echo=True, connect_args=connect_args)

    def deposit(self, transaction: TransactionDTO):
        with Session(self.engine) as session:
            statement = select(User).where(User.username == transaction.username)
            user = session.exec(statement=statement).first()
            transaction_entity = Transaction(
                amount=transaction.amount,
                transaction_type=TransactionType.deposit,
                user_id=user.id,
            )
            session.add(transaction_entity)
            # Here make user.balance += transaction.amount
            session.commit()
