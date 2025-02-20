from pydantic import BaseModel, Field

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
    type_: GameType = Field(alias="type")


class CreateGameResponse(BaseModel):
    game_id: int


class DepositRequest(BaseModel):
    amount: float


class WithdrawRequest(BaseModel):
    amount: float
