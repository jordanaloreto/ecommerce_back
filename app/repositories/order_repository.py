from sqlalchemy.orm import joinedload
from app.models.order_model import Order, OrderItem
from app.models.cart_model import CartItem
from app.connection.database import database

class OrderRepository:
    def create_order_from_cart(self, user_id: int):
        with database.get_session() as session:
            # Busca os itens do carrinho com informações de produtos
            cart_items = (
                session.query(CartItem)
                .join(CartItem.cart)
                .options(joinedload(CartItem.product))  # Carrega os produtos relacionados
                .filter(CartItem.cart.has(user_id=user_id))  # Filtra pelo usuário do carrinho
                .all()
            )

            if not cart_items:
                raise Exception("Carrinho está vazio.")

            # Cria o pedido
            order = Order(user_id=user_id)
            session.add(order)
            session.commit()

            # Adiciona os itens do carrinho ao pedido
            for cart_item in cart_items:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=cart_item.product_id,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,  # Preço atual do produto
                )
                session.add(order_item)

            # Remove os itens do carrinho
            session.query(CartItem).filter(CartItem.cart.has(user_id=user_id)).delete()

            session.commit()

            # Recarrega o pedido com os itens relacionado
            session.refresh(order)

            order = session.query(Order).options(joinedload(Order.items).joinedload(OrderItem.product)).filter(Order.id == order.id).first()
            for item in order.items:
                item.product_name = item.product.name  # Atribui o nome do produto ao item

            return order

    def get_orders_by_user(self, user_id: int):
        with database.get_session() as session:
            orders = (
                session.query(Order)
                .options(
                    joinedload(Order.items).joinedload(OrderItem.product)  # Carrega os produtos relacionados
                )
                .filter(Order.user_id == user_id)
                .all()
            )

            # Adiciona o nome do produto manualmente aos itens do pedido
            for order in orders:
                for item in order.items:
                    item.product_name = item.product.name  # Atribui o nome do produto ao item

            return orders

    def get_order_by_id(self, order_id: int):
        with database.get_session() as session:
            return (
                session.query(Order)
                .options(joinedload(Order.items).joinedload(OrderItem.product))  # Carrega os itens e produtos relacionados
                .filter(Order.id == order_id)
                .first()
            )

