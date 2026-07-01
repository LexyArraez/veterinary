from fastapi import FastAPI
from app.config.settings import settings
from app.config.lifespan import lifespan
from app.routers.customers_router import router as customers_router
from app.routers.pets_router import router as pets_router



app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    lifespan=lifespan,
)

app.include_router(customers_router)
app.include_router(pets_router)