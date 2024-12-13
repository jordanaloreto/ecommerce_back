from fastapi import APIRouter, HTTPException
from app.services.categoria_service import CategoriaService
from app.models.categoria_model import CategoriaResponse, CategoriaCreate

router = APIRouter()
service = CategoriaService()

@router.get("/categorias", response_model=list[CategoriaResponse])
def get_all_categorias():
    return service.get_all_categorias()

@router.get("/categoria/{categoria_id}", response_model=CategoriaResponse)
def get_categoria_by_id(categoria_id: int):
    categoria = service.get_categoria_by_id(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return categoria

@router.post("/categoria/save", response_model=CategoriaResponse)
def create_categoria(categoria: CategoriaCreate):
    return service.create_categoria(categoria)

@router.delete("/categoria/{categoria_id}")
def delete_categoria(categoria_id: int):
    deleted = service.delete_categoria(categoria_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return {"message": "Categoria deleted successfully"}