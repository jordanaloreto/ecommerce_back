from fastapi import APIRouter, HTTPException
from app.services.review_service import ReviewService
from app.models.review_model import ReviewResponse, ReviewCreate

router = APIRouter()
service = ReviewService()

@router.get("/reviews", response_model=list[ReviewResponse])
def get_all_reviews():
    return service.get_all_reviews()

@router.get("/review/{review_id}", response_model=ReviewResponse)
def get_review_by_id(review_id: int):
    review = service.get_review_by_id(review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.get("/reviews/product/{product_id}", response_model=list[ReviewResponse])
def get_reviews_by_product(product_id: int):
    return service.get_reviews_by_product(product_id)

@router.post("/review/save", response_model=ReviewResponse)
def create_review(review: ReviewCreate):
    return service.create_review(review)

@router.put("/review/{review_id}", response_model=ReviewResponse)
def update_review(review_id: int, review_data: ReviewCreate):
    updated_review = service.update_review(review_id, review_data)
    if not updated_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return updated_review

@router.delete("/review/{review_id}")
def delete_review(review_id: int):
    deleted = service.delete_review(review_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"message": "Review deleted successfully"}
