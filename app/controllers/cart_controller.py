# controllers/cart_controller.py
from fastapi import APIRouter, HTTPException
from app.services.cart_service import CartService
from app.models.cart_model import CartResponse, CartItemBase

router = APIRouter()
service = CartService()

@router.get("/cart/{user_id}", response_model=CartResponse)
def get_cart(user_id: int):
    cart = service.get_user_cart(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado.")
    return cart

@router.post("/cart/{user_id}/add", response_model=CartResponse)
def add_product_to_cart(user_id: int, item: CartItemBase):
    try:
        service.add_product_to_cart(user_id, item.product_id, item.quantity)
        return service.get_user_cart(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/cart/{user_id}/remove/{product_id}")
def remove_product_from_cart(user_id: int, product_id: int):
    try:
        service.remove_product_from_cart(user_id, product_id)
        return {"message": "Produto removido do carrinho com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
