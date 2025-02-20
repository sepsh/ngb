from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dto import UserDTO
from src.application.user import UserService

from .models import CreateUserRequest, UserBalanceResponse, UserResponse

router_v0 = APIRouter()


@router_v0.get("/user", tags=["User"], response_model=list[UserResponse])
async def list_users(user_service: UserService = Depends()):
    return user_service.list_users()


@router_v0.get("/user/{username}", tags=["User"], response_model=UserResponse)
async def get_user(username: str, user_service: UserService = Depends()):
    return user_service.get_user(username=username)


@router_v0.post("/user", tags=["User"])
async def create_user(request: CreateUserRequest, user_service: UserService = Depends()):
    user_dto = UserDTO(username=request.username, nickname=request.nickname)
    user_service.create_user(user=user_dto)


@router_v0.get("/user/{username}/balance", tags=["User"], response_model=UserBalanceResponse, deprecated=True)
async def get_user_balance(username: str, user_service: UserService = Depends()):
    balance_dto = user_service.get_balance(username=username)
    if balance_dto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return UserBalanceResponse(amount=balance_dto.amount)
