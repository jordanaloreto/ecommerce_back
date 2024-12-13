from fastapi import APIRouter, HTTPException
from app.services.order_service import OrderService
from app.models.order_model import OrderResponse

router = APIRouter()
service = OrderService()

@router.post("/order/create", response_model=OrderResponse)
def create_order(user_id: int):
    try:
        order = service.create_order_from_cart(user_id)
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/orders/user/{user_id}", response_model=list[OrderResponse])
def get_orders_by_user(user_id: int):
    orders = service.get_orders_by_user(user_id)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return orders

@router.get("/order/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int):
    order = service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
