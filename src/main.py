from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.data.migration import create_db_and_tables
from src.presentation import core_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables() # FIXME move this to deployment
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=core_router)
