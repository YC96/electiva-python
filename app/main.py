from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users.infraestructure.controller.user_controller import router as user_router
from app.common.database.postgresql import Base, engine
from app.products.infrastructure.controllers.products import router as products_router
from app.order.infrastructure.controller.order_controller import router

app = FastAPI(title=" Proyecto Final - API" , description="API para el proyecto final de la materia de Desarrollo de APIs con python", version="1.0.0", routes=[])

Base.metadata.create_all(bind=engine)

#Las rutas de los endpoints
app.include_router(user_router)
app.include_router(products_router, prefix="/api", tags=["products"])
app.include_router(router, prefix="/api/v1", tags=["router"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
