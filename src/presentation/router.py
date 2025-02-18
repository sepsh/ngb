from fastapi import APIRouter

from .v0 import router_v0

core_router = APIRouter()


core_router.include_router(
    router=router_v0,
    prefix="/v0",
)
