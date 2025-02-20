from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import NVARCHAR, Column, DateTime, Field, SQLModel, func

from src.data.enums import GameType


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    nickname: str = Field(sa_column=Column(NVARCHAR))
    balance: float = Field(default=0, max_items=25, decimal_places=5)


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(NVARCHAR))
    description: Optional[str] = Field(sa_column=Column(NVARCHAR))
    type_: GameType
    created_at: datetime = Field(default=datetime.now())


class TransactionType(str, Enum):
    BUY_IN = "BUY_IN"
    CASH_OUT = "CASH_OUT"
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float = Field(default=0, max_items=25, decimal_places=5)
    tr_datetime: datetime | None = Field(sa_column=Column(DateTime, server_default=func.now()))
    transaction_type: TransactionType

    user_id: int = Field(foreign_key="user.id")
