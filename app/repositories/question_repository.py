from app.models.question_model import Question, QuestionCreate
from app.connection.database import database
from sqlalchemy.orm import Session

class QuestionRepository:
    
    def get_all_by_product(self, product_id: int):
        with database.get_session() as session:
            return session.query(Question).filter(Question.product_id == product_id).all()

    def create(self, question_data: QuestionCreate):
        with database.get_session() as session:
            question = Question(
                product_id=question_data.product_id,
                customer_id=question_data.customer_id,
                question=question_data.question
            )
            session.add(question)
            session.commit()
            session.refresh(question)
            return question

    def answer_question(self, question_id: int, answer: str):
        with database.get_session() as session:
            question = session.query(Question).filter(Question.id == question_id).first()
            if question:
                question.answer = answer
                session.commit()
                session.refresh(question)
                return question
            return None
