from typing import Optional

from sqlmodel import Field, SQLModel


class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    started_epoch_64_utc: int
    finished_epoch_64_utc: int


class BuyIn(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    time_epoch_64_utc: int

    player_id: int = Field(foreign_key="player.id")
    game_id: int = Field(foreign_key="game.id")


class CashOut(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    time_epoch_64_utc: int

    player_id: int = Field(foreign_key="player.id")
    game_id: int = Field(foreign_key="game.id")
