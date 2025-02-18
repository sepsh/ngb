from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    nick_name: str


class UserBalanceDTO(BaseModel):
    amount: float
