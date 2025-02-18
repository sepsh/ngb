from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.presentation import core_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=core_router)
