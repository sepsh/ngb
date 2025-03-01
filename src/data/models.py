from datetime import datetime
from enum import Enum
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum as SAEnum, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.data.enums import GameType

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    nickname = Column(String, nullable=True)
    balance = Column(Float, default=0)

    transactions = relationship("Transaction", back_populates="user")


class Game(Base):
    __tablename__ = "game"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    type_ = Column(SAEnum(GameType), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class TransactionType(Enum):
    BUY_IN = "BUY_IN"
    CASH_OUT = "CASH_OUT"
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class Transaction(Base):
    __tablename__ = "transaction"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, default=0, nullable=False)
    tr_datetime = Column(DateTime, server_default=func.now(), nullable=False)
    transaction_type = Column(SAEnum(TransactionType), nullable=False)
    
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="transactions")
