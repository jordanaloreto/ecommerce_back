from app.repositories.categoria_repository import CategoriaRepository
from app.models.categoria_model import CategoriaCreate

class CategoriaService:
    def __init__(self):
        self.repository = CategoriaRepository()   # Instância do repositório

    # Retorna todos os produtos
    def get_all_categorias(self):
        return self.repository.get_all()

    # Retorna um produto pelo ID
    def get_categoria_by_id(self, categoria_id: int):
        return self.repository.get_by_id(categoria_id)

    # Cria um novo produto
    def create_categoria(self, categoria: CategoriaCreate):
        return self.repository.create(categoria)

    # Remove um produto pelo ID
    def delete_categoria(self, categoria_id: int):
        return self.repository.delete(categoria_id)