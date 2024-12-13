# controllers/subcategory_controller.py
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List

from app.models.user_model import UserCreate, UserLogin, UserResponse
from app.services.user_service import UserService

router = APIRouter()
service = UserService()

@router.get("/users", response_model=List[UserResponse])
def get_all_users():
    return service.get_all_users()

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/save", response_model=UserResponse)
def create_user(user_data: UserCreate):
    return service.create_user(user_data)

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.post("/user/login", response_model=str)
def login(user: UserLogin, req: Request):
    dados_autenticacao = service.login(user=user, req=req)
    return dados_autenticacao