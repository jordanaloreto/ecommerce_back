from app.connection.database import database  # Importe a instância do banco
from sqlalchemy.orm import joinedload

from app.models.role_model import Role, RoleCreate

# Simulação de um banco de dados em memória
class RoleRepository:

    def get_all(self):
        with database.get_session() as session:
            return session.query(Role).all()

    def get_by_id(self, role_id: int):
        with database.get_session() as session:
            return session.query(Role).options(joinedload(Role.users)).filter(Role.id == role_id).first()

    def create(self, role_data: RoleCreate):
        with database.get_session() as session:
            db_role = Role(name=role_data.name)
            session.add(db_role)
            session.commit()
            session.refresh(db_role)
            return db_role

    def delete(self, role_id: int):
        with database.get_session() as session:
            role = session.query(Role).filter(Role.id == role_id).first()
            if role:
                session.delete(role)
                session.commit()
                return True
            return False