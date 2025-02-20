from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dto import GameDTO, TransactionDTO, UserDTO
from src.application.game_service import GameService
from src.application.transaction_service import TransactionService
from src.application.user import UserService
from src.data.models import TransactionType
from src.utils.db_dependency import get_session

from .models import (
    CreateGameRequest,
    CreateGameResponse,
    CreateUserRequest,
    DepositRequest,
    UserBalanceResponse,
    UserResponse,
    WithdrawRequest,
)

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


@router_v0.post("/game", tags=["Game"], response_model=CreateGameResponse)
async def create_game(request: CreateGameRequest, game_service: GameService = Depends(), session: get_session = Depends()):
    game_dto = GameDTO(title=request.title, description=request.description, type_=request.type_)
    game_id = game_service.create_game(game=game_dto, session=session)
    return CreateGameResponse(game_id=game_id)


@router_v0.post("/user/{username}/deposit", tags=["User", "Balance"])
async def deposit(
    username: str, request: DepositRequest, transaction_service: TransactionService = Depends(), session: get_session = Depends()
):
    transaction_dto = TransactionDTO(
        username=username,
        amount=request.amount,
        transaction_type=TransactionType.DEPOSIT,
    )
    transaction_service.deposit(transaction=transaction_dto, session=session)


@router_v0.post("/user/{username}/withdraw", tags=["User", "Balance"])
async def withdraw(
    username: str, request: WithdrawRequest, transaction_service: TransactionService = Depends(), session: get_session = Depends()
): ...
