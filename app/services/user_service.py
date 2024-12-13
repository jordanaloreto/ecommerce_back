# services/subcategory_service.py
from typing import List, Optional

from fastapi import Request
from fastapi.responses import JSONResponse

from app.models.subcategory_model import SubCategoryCreate
from app.models.user_model import UserCreate, UserLogin, UserResponse
from app.repositories.user_repository import UserRepository
from app.utils.settings import settings
from jose import jwt

class UserService:

    def __init__(self):
        self.repository = UserRepository()  # Instância do repositório de categorias

    def login(self, user: UserLogin, req: Request):

        user_db = self.get_user_by_user_name(user_name=user.user_name)

        if not user_db or user_db.password != user.password:
            return JSONResponse(
                status_code=401,
                content="usuário não encontrado!",
            )
            

        payload = {
            "user_name": user_db.user_name,
            "user_id": user_db.id,
            "role_id": user_db.role_id
        }

        access_token = jwt.encode(payload, settings.jwt_key, settings.jwt_algorithm)

        return access_token

    # Retorna todas as categorias
    def get_all_users(self):
        return self.repository.get_all()

    # Retorna uma categoria pelo ID
    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
    
    def get_user_by_user_name(self, user_name: int):
        return self.repository.get_by_user_name(user_name)

    # Cria uma nova categoria
    def create_user(self, user: UserCreate):
        return self.repository.create(user)

    # Remove uma categoria pelo ID
    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)

