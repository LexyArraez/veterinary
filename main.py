from fastapi import FastAPI
from app.routers.routers_home import router as home_router
from app.config.settings import settings
from app.database.db_connection import engine, Base
from sqlalchemy import text
from app.routers.customers_router import router as customers_router
from app.models.customers_models import CustomerModel
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description
)

app.include_router(home_router)
app.include_router(customers_router)

@app.get("/health-db", tags=["health"])
def db_check():
    with engine.connect() as connection:
        connection.execute(text('SELECT 1'))
    return{"message": "DB Health check successful"}
