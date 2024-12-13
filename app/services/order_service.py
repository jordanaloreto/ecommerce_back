from app.repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self):
        self.repository = OrderRepository()

    def create_order_from_cart(self, user_id: int):
        return self.repository.create_order_from_cart(user_id)

    def get_orders_by_user(self, user_id: int):
        return self.repository.get_orders_by_user(user_id)

    def get_order_by_id(self, order_id: int):
        return self.repository.get_order_by_id(order_id)
