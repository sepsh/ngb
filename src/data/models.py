from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import NVARCHAR, Column, Field, SQLModel

from src.data.enums import GameType


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    nickname: str = Field(sa_column=Column(NVARCHAR))
    balance: Decimal = Field(default=0, max_items=25, decimal_places=5)


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(NVARCHAR))
    description: Optional[str] = Field(sa_column=Column(NVARCHAR))
    type_: GameType
    created_at: datetime = Field(default=datetime.now())
