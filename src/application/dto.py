from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    username: str
    nickname: str
    balance: float | None = Field(default=None)


class UserBalanceDTO(BaseModel):
    amount: float
