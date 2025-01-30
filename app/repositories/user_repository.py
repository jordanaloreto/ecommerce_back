from sqlalchemy.orm import joinedload
from app.connection.database import database
from app.models.role_model import Role
from app.models.user_model import User, UserCreate

class UserRepository:

    def get_all(self):
        with database.get_session() as session:
            return session.query(User).options(joinedload(User.role)).all()

    def get_by_id(self, user_id: int):
        with database.get_session() as session:
            return session.query(User).options(joinedload(User.role)).filter(User.id == user_id).first()

    
    def get_by_user_name(self, user_name: int):
        with database.get_session() as session:
            return session.query(User).filter(User.user_name == user_name).first()

    def create(self, user_data: UserCreate):
        with database.get_session() as session:
            # Cria a nova subcategoria
            db_user = User(
                user_name=user_data.user_name,
                password=user_data.password,
                role_id=user_data.role_id  # Associa a subcategoria a uma role existente
            )
            session.add(db_user)
            session.commit()
            session.refresh(db_user)

            db_user = session.query(User).options(joinedload(User.role)).filter(User.id == db_user.id).first()

            return db_user
        
    def update(self, user_id: int, user_data: UserCreate):
        with database.get_session() as session:
            # Busca o usuário pelo ID e carrega a role associada
            user = session.query(User).options(joinedload(User.role)).filter(User.id == user_id).first()
            if not user:
                return None  # Retorna None se o usuário não for encontrado

            # Atualiza os campos do usuário
            user.user_name = user_data.user_name
            user.password = user_data.password
            user.role_id = user_data.role_id

            session.commit()  # Confirma a transação
            session.refresh(user)  # Atualiza o objeto com os dados mais recentes do banco

            return user  # Retorna o usuário atualizado

    def delete(self, user_id: int):
        with database.get_session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False