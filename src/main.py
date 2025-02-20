from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.data.migration import create_db_and_tables
from src.presentation import core_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # FIXME move this to deployment
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=core_router)
