import uuid
from fastapi import APIRouter, Depends, HTTPException
from app.users.application.user_service import UserService
from app.users.domain.entities.user_entities import UserCreate, UserEntity, UserUpdate
from app.users.domain.entities.user_login import UserLogin
from app.users.infraestructure.repository.user_repository import SqlAlchemyUserRepository
from app.common.database.postgresql import get_db
from sqlalchemy.orm import Session
from app.auth.infraestructure.auth_controller import JWTService
from app.auth.application.auth_service import AuthUseCase

router = APIRouter()

@router.post("/users/register", response_model=UserEntity)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    hashed_password = JWTService().encrypt_password(user.hashed_password)
    user.hashed_password = hashed_password
    response = user_service.create_user(user)
    if not response:
        raise HTTPException(status_code=404, detail="Fallo registrar al usuario")
    return response

@router.post("/users/managers", response_model=UserEntity)
async def register_manager(user: UserCreate, db: Session = Depends(get_db)):
    if user.role.value != 'manager':
        raise HTTPException(status_code=404, detail="El rol no es válido debe ser un gerente")
    user_service = UserService(SqlAlchemyUserRepository(db))
    hashed_password = JWTService().encrypt_password(user.hashed_password)
    user.hashed_password = hashed_password
    response = user_service.create_user(user)
    if not response:
        raise HTTPException(status_code=404, detail="Fallo registrar al usuario")
    return response

@router.get("/users/managers", response_model=list[UserEntity])
async def get_managers(db: Session = Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    response = user_service.find_user_by_role('manager')
    if not response:
        raise HTTPException(status_code=404, detail="No se encontraron gerentes")
    return response

@router.put("/users/manager/{manager_id}", response_model=UserEntity)
async def update_manager(body: UserUpdate, manager_id: uuid.UUID, db: Session = Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    is_user_exists = user_service.find_user_by_id(manager_id)
    if not is_user_exists:
        raise HTTPException(status_code=404, detail="No se encontró al gerente")
    body.id = manager_id
    response = user_service.update_user(body)
    if not response:
        raise HTTPException(status_code=404, detail="Fallo actualizar al gerente")
    return response

@router.delete("/users/manager/{manager_id}")
async def delete_manager(manager_id: uuid.UUID, db: Session = Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    is_user_exists = user_service.find_user_by_id(manager_id)
    if not is_user_exists:
        raise HTTPException(status_code=404, detail="No se encontró al gerente")
    user_service.delete_user(manager_id)
    return {"msg": "Gerente eliminado exitosamente"}

@router.put("/users/{user_id}", response_model=UserEntity)
async def update_user_by_id(body: UserUpdate, user_id: uuid.UUID, db: Session = Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    is_user_exists = user_service.find_user_by_id(user_id)
    if not is_user_exists:
        raise HTTPException(status_code=404, detail="No se encontró al usuario")
    body.id = user_id
    response = user_service.update_user(body)
    if not response:
        raise HTTPException(status_code=404, detail="Fallo actualizar al usuario")
    return response

@router.post("/users/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    auth_service = AuthUseCase(JWTService(), SqlAlchemyUserRepository(db))
    try:
        return auth_service.login(user)
        return {"access_token": access_token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))