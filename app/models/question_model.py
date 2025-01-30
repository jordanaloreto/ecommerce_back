from sqlalchemy import Column, ForeignKey, Integer, String, Text
from pydantic import BaseModel
from app.connection.database import Base
from sqlalchemy.orm import relationship

# Modelo SQLAlchemy para Perguntas e Respostas
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_id = Column(Integer)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=True)

    product = relationship("Product", back_populates="questions")

# Schemas Pydantic
class QuestionBase(BaseModel):
    product_id: int
    customer_id: int
    question: str

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    answer: str | None
