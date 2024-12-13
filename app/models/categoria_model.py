from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.connection.database import Base
from sqlalchemy.orm import relationship

# from app.models.subcategory_model import SubCategoryResponse


# Definição do modelo SQLAlchemy
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
 # Relacionamento um-para-muitos com SubCategory
    # subcategories = relationship("SubCategory", back_populates="category")
# Definindo a estrutura básica de um produto
class CategoriaBase(BaseModel):
    name: str # Nome do produto

# Modelo usado na criação de um novo produto
class CategoriaCreate(CategoriaBase):
    pass  # Não há novos campos além dos de ProductBase

# Modelo com o ID incluído, usado para leitura de dados
class CategoriaResponse(CategoriaBase):
    id: int
    # subcategories: list["SubCategoryResponse"] = []
