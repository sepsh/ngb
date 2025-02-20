from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    nickname: str


class UserBalanceResponse(BaseModel):
    amount: float
