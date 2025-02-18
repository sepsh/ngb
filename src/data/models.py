from decimal import Decimal
from typing import Optional

from sqlmodel import NVARCHAR, Column, Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    nick_name: str = Field(sa_column=Column(NVARCHAR))
    balance: Decimal = Field(default=0, max_items=25, decimal_places=5)
