from pydantic import BaseModel

from src.data.enums import GameType


class CreateUserRequest(BaseModel):
    username: str
    nickname: str


class UserBalanceResponse(BaseModel):
    amount: float


class UserResponse(BaseModel):
    username: str
    nickname: str
    balance: float


class CreateGameRequest(BaseModel):
    title: str
    description: str | None
    type_: GameType


class CreateGameResponse(BaseModel):
    game_id: int
