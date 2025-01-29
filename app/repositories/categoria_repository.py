from app.models.categoria_model import Categoria, CategoriaCreate
from app.connection.database import database  # Importe a instância do banco
from sqlalchemy.orm import joinedload

# Simulação de um banco de dados em memória
class CategoriaRepository:

    def get_all(self):
        with database.get_session() as session:
            return session.query(Categoria).all()

    def get_by_id(self, categoria_id: int):
        with database.get_session() as session:
            return session.query(Categoria).options(joinedload(Categoria.subcategories)).filter(Categoria.id == categoria_id).first()

    def create(self, categoria_data: CategoriaCreate):
        with database.get_session() as session:
            db_categoria = Categoria(name=categoria_data.name)
            session.add(db_categoria)
            session.commit()
            session.refresh(db_categoria)
            return db_categoria
        
    def update(self, categoria_id: int, categoria_data: CategoriaCreate):
        with database.get_session() as session:
            categoria = session.query(Categoria).filter(Categoria.id == categoria_id).first()
            if not categoria:
                return None
            categoria.name = categoria_data.name  # Atualiza o nome
            session.commit()
            session.refresh(categoria)
            return categoria


    def delete(self, categoria_id: int):
        with database.get_session() as session:
            categoria = session.query(Categoria).filter(Categoria.id == categoria_id).first()
            if categoria:
                session.delete(categoria)
                session.commit()
                return True
            return False