from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.connection.database import Base
from app.models.categoria_model import CategoriaResponse

# Modelo da entidade SubCategory
class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # Relacionamento de volta para Category
    categoria = relationship("Categoria")


class SubCategoryBase(BaseModel):
    name: str
    categoria_id: int


class SubCategoryCreate(SubCategoryBase):
    pass


class SubCategoryResponse(SubCategoryBase):
    id: int
    categoria: "CategoriaResponse"

