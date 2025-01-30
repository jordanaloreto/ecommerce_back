from app.repositories.question_repository import QuestionRepository
from app.models.question_model import QuestionCreate

class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()

    def get_questions_for_product(self, product_id: int):
        return self.repository.get_all_by_product(product_id)

    def create_question(self, question_data: QuestionCreate):
        return self.repository.create(question_data)

    def answer_question(self, question_id: int, answer: str, is_admin: bool):
        if not is_admin:
            raise ValueError("Only administrators can answer questions.")
        return self.repository.answer_question(question_id, answer)
