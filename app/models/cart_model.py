# models/cart_model.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.connection.database import Base
from pydantic import BaseModel
from typing import List

# Modelo SQLAlchemy para o Carrinho
class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Relacionamento com o usuário
    items = relationship("CartItem", back_populates="cart")  # Itens do carrinho

# Modelo SQLAlchemy para os Itens do Carrinho
class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)

    # Relacionamento com o carrinho
    cart = relationship("Cart", back_populates="items")

    # Relacionamento com o produto
    product = relationship("Product")


# Schemas Pydantic
class CartItemBase(BaseModel):
    product_id: int
    quantity: int

class CartItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str  # Nome do produto
    product_price: float  # Preço do produto
    quantity: int


class CartResponse(BaseModel):
    id: int
    user_id: int
    items: List[CartItemResponse]



