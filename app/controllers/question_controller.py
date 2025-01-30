from fastapi import APIRouter, HTTPException, Depends
from app.services.question_service import QuestionService
from app.models.question_model import QuestionCreate
from typing import List

router = APIRouter()
service = QuestionService()

@router.get("/product/{product_id}/questions", response_model=List[QuestionCreate])
def get_questions_for_product(product_id: int):
    return service.get_questions_for_product(product_id)

@router.post("/product/question", response_model=QuestionCreate)
def create_question(question: QuestionCreate):
    return service.create_question(question)

@router.put("/product/question/{question_id}/answer")
def answer_question(question_id: int, answer: str, is_admin: bool = Depends(lambda: True)):  # Simulando autenticação
    try:
        updated_question = service.answer_question(question_id, answer, is_admin)
        if not updated_question:
            raise HTTPException(status_code=404, detail="Question not found")
        return updated_question
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
