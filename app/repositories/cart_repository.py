# repository/cart_repository.py
from app.models.cart_model import Cart, CartItem
from app.connection.database import database
from sqlalchemy.orm import joinedload

class CartRepository:
    # Obter o carrinho do usuário
    def get_cart_by_user_id(self, user_id: int):
            with database.get_session() as session:
                # Busca o carrinho do usuário e carrega os itens com os produtos
                cart = (
                    session.query(Cart)
                    .options(joinedload(Cart.items).joinedload(CartItem.product))
                    .filter(Cart.user_id == user_id)
                    .first()
                )

                if not cart:
                    return None

                # Preenche os itens do carrinho com informações do produto
                for item in cart.items:
                    item.product_name = item.product.name
                    item.product_price = item.product.price

                return cart

    # Criar um novo carrinho para o usuário
    def create_cart(self, user_id: int):
        with database.get_session() as session:
            new_cart = Cart(user_id=user_id)
            session.add(new_cart)
            session.commit()
            session.refresh(new_cart)
            return new_cart

    # Adicionar item ao carrinho
    def add_item_to_cart(self, cart_id: int, product_id: int, quantity: int):
        with database.get_session() as session:
            # Verifica se o produto já está no carrinho
            cart_item = session.query(CartItem).filter(
                CartItem.cart_id == cart_id,
                CartItem.product_id == product_id
            ).first()

            if cart_item:
                # Se o produto já existir, aumenta a quantidade
                cart_item.quantity += quantity
            else:
                # Caso contrário, cria um novo item no carrinho
                cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
                session.add(cart_item)

            session.commit()
            session.refresh(cart_item)
            return cart_item



    def remove_item_from_cart(self, cart_id: int, product_id: int):
        with database.get_session() as session:
            # Busca o item no carrinho
            cart_item = session.query(CartItem).filter(
                CartItem.cart_id == cart_id, CartItem.product_id == product_id
            ).first()

            if cart_item:
                if cart_item.quantity > 1:
                    # Diminui a quantidade do item
                    cart_item.quantity -= 1
                else:
                    # Remove o item completamente se a quantidade for 1
                    session.delete(cart_item)

                # Salva as mudanças no banco de dados
                session.commit()
                return True

            return False


