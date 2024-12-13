from typing import List
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel
from app.connection.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())  # Data e hora do pedido
    items = relationship("OrderItem", back_populates="order")  # Itens do pedido

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
    price = Column(Float)  # Preço do produto no momento do pedido

    order = relationship("Order", back_populates="items")  # Relacionamento com o pedido
    product = relationship("Product")  # Relacionamento com o produto

    from typing import List
from datetime import datetime

# Esquema para itens do pedido
class OrderItemBase(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float

class OrderItemResponse(OrderItemBase):
    id: int

# Esquema para pedidos
class OrderBase(BaseModel):
    user_id: int

class OrderCreate(OrderBase):
    items: List[OrderItemBase]  # Lista de itens no pedido

class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    items: List[OrderItemResponse]


