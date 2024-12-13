# services/cart_service.py
from app.repositories.cart_repository import CartRepository

class CartService:
    def __init__(self):
        self.repository = CartRepository()

    def get_user_cart(self, user_id: int):
        return self.repository.get_cart_by_user_id(user_id)

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int):
        # Tenta obter o carrinho do usuário
        cart = self.repository.get_cart_by_user_id(user_id)
        
        # Se o carrinho não existir, cria um novo
        if not cart:
            cart = self.repository.create_cart(user_id)
        
        # Adiciona o item ao carrinho
        return self.repository.add_item_to_cart(cart.id, product_id, quantity)


    def remove_product_from_cart(self, user_id: int, product_id: int):
        cart = self.repository.get_cart_by_user_id(user_id)
        if not cart:
            raise Exception("Carrinho não encontrado para o usuário.")
        return self.repository.remove_item_from_cart(cart.id, product_id)
