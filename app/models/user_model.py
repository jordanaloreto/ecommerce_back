from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.connection.database import Base
from app.models.role_model import RoleResponse

# Modelo da entidade User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    # Relacionamento de volta para Category
    role = relationship("Role", lazy="joined")


class UserBase(BaseModel):
    user_name: str
    password: str
    role_id: int


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    role: RoleResponse

class UserLogin(BaseModel):
    user_name: str
    password: str
