from fastapi import FastAPI
from app.order.infrastructure.controller.order_controller import router
from app.order.infrastructure.database.database_config import Base ,engine
from app.products.infrastructure.controllers.products import router as products_router

Base.metadata.create_all(bind=engine)

app = FastAPI(routes=[])

#Las rutas de los endpoints
app.include_router(products_router, prefix="/api", tags=["products"])
app.include_router(router, prefix="/api/v1", tags=["router"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
