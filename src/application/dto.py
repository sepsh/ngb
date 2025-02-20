from pydantic import BaseModel, Field

from src.data.enums import GameType


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
