from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    nickname: str


class UserBalanceDTO(BaseModel):
    amount: float
