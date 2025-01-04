from fastapi import FastAPI
from app.products.infrastructure.controllers.products import router as products_router

app = FastAPI(routes=[])

app.include_router(products_router, prefix="/api", tags=["products"])