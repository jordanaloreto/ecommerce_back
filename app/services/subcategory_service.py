# services/subcategory_service.py
from app.models.subcategory_model import SubCategoryResponse, SubCategoryCreate
from app.repositories.subcategory_repository import SubCategoryRepository
from typing import List, Optional

class SubCategoryService:
    def __init__(self):
        self.repository = SubCategoryRepository()

    def get_all_subcategories(self) -> List[SubCategoryResponse]:
        return self.repository.get_all()

    def get_subcategory_by_id(self, subcategory_id: int) -> Optional[SubCategoryResponse]:
        return self.repository.get_by_id(subcategory_id)

    def create_subcategory(self, subcategory_data: SubCategoryCreate) -> SubCategoryResponse:
        return self.repository.create(subcategory_data)
    
    def update_subcategory(self, subcategory_id: int, subcategory_data: SubCategoryCreate):
        return self.repository.update(subcategory_id, subcategory_data)

     # Remove um produto pelo ID
    def delete_subcategory(self, subcategory_id: int):
        return self.repository.delete(subcategory_id)
