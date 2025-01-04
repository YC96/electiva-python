from fastapi import FastAPI
from app.products.infrastructure.controllers.products import controller as products_controller

app = FastAPI(routes=[])

app.include_router(products_controller, prefix="/api", tags=["products"])