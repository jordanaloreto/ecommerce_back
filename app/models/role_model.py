from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.connection.database import Base
from sqlalchemy.orm import relationship

# from app.models.subcategory_model import SubCategoryResponse


# Definição do modelo SQLAlchemy
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
 
# Definindo a estrutura básica de um produto
class RoleBase(BaseModel):
    name: str # Nome do produto

# Modelo usado na criação de um novo produto
class RoleCreate(RoleBase):
    pass  # Não há novos campos além dos de ProductBase

# Modelo com o ID incluído, usado para leitura de dados
class RoleResponse(RoleBase):
    id: int
    # subcategories: list["SubCategoryResponse"] = []
