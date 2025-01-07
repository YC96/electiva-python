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
async def register_user(user: UserEntity, db: Session= Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    response = user_service.create_user(user)
    if not response:
      raise HTTPException(status_code=404, detail="Fallo registrar al usuario")
    return response

@router.post("/users/managers", response_model=UserEntity)
async def register_manager(user: UserEntity, db: Session= Depends(get_db)):
    print(user.role.value)
    if user.role.value != 'manager':
      raise HTTPException(status_code=404, detail="El rol no es válido debe ser un gerente")
    user_service = UserService(SqlAlchemyUserRepository(db))
    response = user_service.create_user(user)
    if not response:
      raise HTTPException(status_code=404, detail="Fallo registrar al usuario")
    return response

@router.get("/users/managers", response_model=list[UserCreate])
async def get_managers(db: Session= Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    response = user_service.find_user_by_role('manager')
    if not response:
      raise HTTPException(status_code=404, detail="No se encontraron gerentes")
    print(response)
    return response

@router.put("/users/manager{managers_id}", response_model=UserCreate)
async def update_manager(body: UserUpdate, managers_id: uuid.UUID, db: Session= Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    is_user_exits = user_service.find_user_by_id(f'{managers_id}')
    if not is_user_exits:
      raise HTTPException(status_code=404, detail="No se encontró al gerente")
    for key, value in body.dict().items():
      if value is None:
        setattr(body, key, getattr(is_user_exits, key))
    response = user_service.update_user(body)
    if not response:
      raise HTTPException(status_code=404, detail="Fallo actualizar al gerente")
    return response

@router.delete("/users/manager{managers_id}")
async def delete_manager(managers_id: uuid.UUID, db: Session= Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    is_user_exits = user_service.find_user_by_id(f'{managers_id}')
    if not is_user_exits:
      raise HTTPException(status_code=404, detail="No se encontró al gerente")
    response = user_service.delete_user(is_user_exits)
    if not response:
      raise HTTPException(status_code=404, detail="Fallo eliminar al gerente")
    return response

@router.put("/users/{user_id}", response_model=UserCreate)
async def update_user_by_id(body: UserUpdate, user_id: uuid.UUID, db: Session= Depends(get_db)):
    user_service = UserService(SqlAlchemyUserRepository(db))
    is_user_exits = user_service.find_user_by_id(f'{user_id}')
    if not is_user_exits:
      raise HTTPException(status_code=404, detail="No se encontró al gerente")
    for key, value in body.dict().items():
      if value is None:
        setattr(body, key, getattr(is_user_exits, key))
    response = user_service.update_user(body)
    if not response:
      raise HTTPException(status_code=404, detail="Fallo actualizar al gerente")
    return response

@router.post("/users/login")
async def login_user(user: UserLogin, db: Session= Depends(get_db)):
    auth_service = AuthUseCase(JWTService(), SqlAlchemyUserRepository(db))
    response = auth_service.login(user)
    if not response:
      raise HTTPException(status_code=404, detail="Fallo iniciar sesión")
    return response