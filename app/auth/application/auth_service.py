from app.auth.infraestructure.auth_controller import JWTService
from app.users.infraestructure.repository.user_repository import SqlAlchemyUserRepository
from app.users.domain.entities.user_login import UserLogin

class AuthUseCase:
    def __init__(self, jwt_service: JWTService, user_repository: SqlAlchemyUserRepository):
        self.jwt_service = jwt_service
        self.user_repository = user_repository

    def login(self, user: UserLogin):
        user_bd = self.user_repository.find_by_email(user.email)
        print(user_bd.email)
        print(user.hashed_password)
        print(user_bd.hashed_password)
        if not user_bd:
            raise ValueError("Usuario no encontrado")
        if not self.jwt_service.verify_password(user.hashed_password, user_bd.hashed_password):
            raise ValueError("Contraseña incorrecta")
        return self.jwt_service.create_access_token(data={"sub": user.email})
