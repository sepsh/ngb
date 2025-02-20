from sqlalchemy import Engine
from sqlmodel import Session, create_engine, func, select, update

from src.application.dto import TransactionDTO
from src.data.models import Transaction, TransactionType, User


class TransactionService:
    def deposit(self, transaction: TransactionDTO, session: Session):
        with session as session:
            statement = select(User).where(User.username == transaction.username).with_for_update()
            user = session.exec(statement).first()

            if not user:
                raise ValueError("User not found")

            # Create the transaction record
            transaction_entity = Transaction(
                amount=transaction.amount,
                transaction_type=TransactionType.DEPOSIT,
                user_id=user.id,
            )
            session.add(transaction_entity)

            # Update balance using a database function (atomic update)
            session.exec(update(User).where(User.id == user.id).values(balance=User.balance + transaction.amount))

            session.commit()
