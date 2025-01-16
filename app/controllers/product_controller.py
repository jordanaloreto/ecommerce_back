from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.models.product_model import ProductResponse, ProductCreate

router = APIRouter()
service = ProductService()

@router.get("/products", response_model=list[ProductResponse])
def get_all_products():
    return service.get_all_products()

@router.get("/product/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    product = service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/products/subcategory/{subcategory_id}", response_model=list[ProductResponse])
def get_by_subcategory(subcategory_id: int):
    products = service.get_by_subcategory(subcategory_id)
    return products

@router.post("/product/save", response_model=ProductResponse)
def create_product(product: ProductCreate):
    return service.create_product(product)

@router.delete("/product/{product_id}")
def delete_product(product_id: int):
    deleted = service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}