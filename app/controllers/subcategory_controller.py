# controllers/subcategory_controller.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.subcategory_model import SubCategoryCreate, SubCategoryResponse
from app.services.subcategory_service import SubCategoryService

router = APIRouter()
service = SubCategoryService()

@router.get("/subcategories", response_model=List[SubCategoryResponse])
def get_all_subcategories():
    return service.get_all_subcategories()

@router.get("/subcategories/{subcategory_id}", response_model=SubCategoryResponse)
def get_subcategory_by_id(subcategory_id: int):
    subcategory = service.get_subcategory_by_id(subcategory_id)
    if subcategory is None:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    return subcategory

@router.post("/subcategories/save", response_model=SubCategoryResponse)
def create_subcategory(subcategory_data: SubCategoryCreate):
    return service.create_subcategory(subcategory_data)

@router.delete("/subcategories/{subcategory_id}")
def delete_subcategory(subcategory_id: int):
    deleted = service.delete_subcategory(subcategory_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return {"message": "Categoria deleted successfully"}
