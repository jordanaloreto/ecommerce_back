from sqlalchemy.orm import joinedload
from app.models.categoria_model import Categoria
from app.models.subcategory_model import SubCategory, SubCategoryCreate
from app.connection.database import database

class SubCategoryRepository:

    def get_all(self):
        with database.get_session() as session:
            return session.query(SubCategory).options(joinedload(SubCategory.categoria)).all()

    def get_by_id(self, subcategory_id: int):
        with database.get_session() as session:
            return session.query(SubCategory).options(joinedload(SubCategory.categoria)).filter(SubCategory.id == subcategory_id).first()

    def create(self, subcategory_data: SubCategoryCreate):
        with database.get_session() as session:
            # Cria a nova subcategoria
            db_subcategory = SubCategory(
                name=subcategory_data.name,
                categoria_id=subcategory_data.categoria_id  # Associa a subcategoria a uma categoria existente
            )
            session.add(db_subcategory)
            session.commit()
            session.refresh(db_subcategory)

            # Busca a categoria correspondente e retorna junto com a subcategoria
            db_categoria = session.query(Categoria).filter(Categoria.id == db_subcategory.categoria_id).first()
            db_subcategory.categoria = db_categoria  # Atribui a categoria ao objeto da subcategoria

            return db_subcategory

    from sqlalchemy.orm import joinedload

    def update(self, subcategory_id: int, subcategory_data: SubCategoryCreate):
        with database.get_session() as session:
            # Busca a subcategoria pelo ID e carrega a categoria associada
            subcategory = session.query(SubCategory).options(joinedload(SubCategory.categoria)).filter(SubCategory.id == subcategory_id).first()
            if not subcategory:
                return None

            # Verifica se a categoria_id fornecida existe
            categoria = session.query(Categoria).filter(Categoria.id == subcategory_data.categoria_id).first()
            if not categoria:
                raise ValueError("Categoria não encontrada")

            # Atualiza os campos da subcategoria
            subcategory.name = subcategory_data.name
            subcategory.categoria_id = subcategory_data.categoria_id

            session.commit()
            session.refresh(subcategory)

            return subcategory

    def delete(self, subcategory_id: int):
        with database.get_session() as session:
            subcategory = session.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
            if subcategory:
                session.delete(subcategory)
                session.commit()
                return True
            return False