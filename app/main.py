from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users.infraestructure.controller.user_controller import router as user_router
from app.common.database.postgresql import Base, engine

app = FastAPI(title=" Proyecto Final - API" , description="API para el proyecto final de la materia de Desarrollo de APIs con python", version="1.0.0", routes=[])

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)