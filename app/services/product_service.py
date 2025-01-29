from app.repositories.product_repository import ProductRepository
from app.models.product_model import ProductCreate

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()   # Instância do repositório

    # Retorna todos os produtos
    def get_all_products(self):
        return self.repository.get_all()
    
     # Retorna produtos pela subcategoria
    def get_by_subcategory(self, subcategory_id: int):
        return self.repository.get_by_subcategory(subcategory_id)

    # Retorna um produto pelo ID
    def get_product_by_id(self, product_id: int):
        return self.repository.get_by_id(product_id)

    # Cria um novo produto
    def create_product(self, product: ProductCreate):
        return self.repository.create(product)
    
    def update_product(self, product_id: int, product_data: ProductCreate):
        return self.repository.update(product_id, product_data)
    # Remove um produto pelo ID
    def delete_product(self, product_id: int):
        return self.repository.delete(product_id)