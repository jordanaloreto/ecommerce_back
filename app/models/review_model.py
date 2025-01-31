from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.connection.database import Base
from app.models.product_model import ProductResponse


# Modelo SQLAlchemy
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    rating = Column(Float, nullable=False)

    product = relationship("Product", back_populates="reviews", lazy="joined")

# Schemas Pydantic
class ReviewBase(BaseModel):
    product_id: int
    user_id: int
    rating: float

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    product: ProductResponse
