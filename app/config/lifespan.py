from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.db_connection import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield