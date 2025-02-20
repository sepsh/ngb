from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from src.data.enums import GameType
from src.data.models import TransactionType


class UserDTO(BaseModel):
    username: str
    nickname: str
    balance: float | None = Field(default=None)


class UserBalanceDTO(BaseModel):
    amount: float


class GameDTO(BaseModel):
    title: str
    description: str | None
    type_: GameType


class TransactionDTO(BaseModel):
    id: Optional[int] = Field(default=None)
    amount: float
    tr_datetime_: Optional[datetime] = Field(default=None)
    transaction_type: TransactionType
    username: str
