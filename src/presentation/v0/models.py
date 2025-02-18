from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    nick_name: str


class UserBalanceResponse(BaseModel):
    amount: float
