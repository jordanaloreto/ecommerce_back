
from app.models.role_model import RoleCreate
from app.repositories.role_repository import RoleRepository


class RoleService:
    def __init__(self):
        self.repository = RoleRepository()   # Instância do repositório

    # Retorna todos os produtos
    def get_all_roles(self):
        return self.repository.get_all()

    # Retorna um produto pelo ID
    def get_role_by_id(self, role_id: int):
        return self.repository.get_by_id(role_id)

    # Cria um novo produto
    def create_role(self, categoria: RoleCreate):
        return self.repository.create(categoria)

    # Remove um produto pelo ID
    def delete_role(self, role_id: int):
        return self.repository.delete(role_id)