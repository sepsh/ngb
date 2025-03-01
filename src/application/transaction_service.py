from sqlalchemy import Engine, func
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.sql.expression import update

from src.application.dto import TransactionDTO
from src.data.models import Transaction, TransactionType, User


class TransactionService:
    def deposit(self, transaction: TransactionDTO, session: Session):
        statement = select(User).where(User.username == transaction.username).with_for_update()
        user = session.scalars(statement).first()

        if not user:
            raise ValueError("User not found")

        # Create the transaction record
        transaction_entity = Transaction(
            amount=transaction.amount,
            transaction_type=TransactionType.DEPOSIT,
            user_id=user.id,
        )
        session.add(transaction_entity)

        # Atomic update of balance
        session.execute(
            update(User)
            .where(User.id == user.id)
            .values(balance=func.coalesce(User.balance, 0) + transaction.amount)
        )

        session.commit()

    def withdraw(self, transaction: TransactionDTO, session: Session):
        statement = select(User).where(User.username == transaction.username).with_for_update()
        user = session.scalars(statement).first()

        if not user:
            raise ValueError("User not found")

        if transaction.amount > user.balance:
            raise ValueError("Insufficient balance")

        # Create the transaction record
        transaction_entity = Transaction(
            amount=transaction.amount,
            transaction_type=TransactionType.WITHDRAWAL,  # Fixed type
            user_id=user.id,
        )
        session.add(transaction_entity)

        # Atomic update of balance
        session.execute(
            update(User)
            .where(User.id == user.id)
            .values(balance=User.balance - transaction.amount)
        )

        session.commit()
