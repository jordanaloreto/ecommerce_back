# app/models/product.py
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from pydantic import BaseModel
from app.connection.database import Base
from sqlalchemy.orm import relationship

from app.models.subcategory_model import SubCategoryResponse

# Definição do modelo SQLAlchemy
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    sub_category_id = Column(Integer, ForeignKey("subcategories.id"))  # Chave estrangeira para SubCategory
    sub_category = relationship("SubCategory", lazy="joined")
    questions = relationship("Question", back_populates="product", lazy="joined")
    average_rating = Column(Float, default=0.0)  
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
# Definição dos schemas Pydantic
class ProductBase(BaseModel):
    name: str
    price: float
    sub_category_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    sub_category: SubCategoryResponse

    # class Config:
    #     orm_mode = True