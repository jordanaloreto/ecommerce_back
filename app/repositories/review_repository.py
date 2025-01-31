from app.models.review_model import Review, ReviewCreate
from app.models.product_model import Product
from app.connection.database import database  # Importe a instância do banco
from sqlalchemy.orm import joinedload

class ReviewRepository:

    def get_all(self):
        with database.get_session() as session:
            return session.query(Review).options(joinedload(Review.product)).all()

    def get_by_product(self, product_id: int):
        with database.get_session() as session:
            return session.query(Review).options(joinedload(Review.product)).filter(Review.product_id == product_id).all()

    def get_by_id(self, review_id: int):
        with database.get_session() as session:
            return session.query(Review).options(joinedload(Review.product)).filter(Review.id == review_id).first()

    def create(self, review_data: ReviewCreate):
        with database.get_session() as session:
            db_review = Review(
                product_id=review_data.product_id,
                user_id=review_data.user_id,
                rating=review_data.rating
            )
            session.add(db_review)
            session.commit()
            session.refresh(db_review)

            # Atualiza a média de avaliações do produto
            self.update_product_rating(session, review_data.product_id)

            return session.query(Review).options(joinedload(Review.product)).filter(Review.id == db_review.id).first()

    def update(self, review_id: int, review_data: ReviewCreate):
        with database.get_session() as session:
            review = session.query(Review).filter(Review.id == review_id).first()
            if not review:
                return None
            
            review.rating = review_data.rating
            session.commit()
            session.refresh(review)

            # Atualiza a média de avaliações do produto
            self.update_product_rating(session, review.product_id)

            return session.query(Review).options(joinedload(Review.product)).filter(Review.id == review.id).first()

    def delete(self, review_id: int):
        with database.get_session() as session:
            review = session.query(Review).filter(Review.id == review_id).first()
            if review:
                product_id = review.product_id
                session.delete(review)
                session.commit()

                # Atualiza a média de avaliações do produto após a exclusão
                self.update_product_rating(session, product_id)
                return True
            return False

    def update_product_rating(self, session, product_id: int):
        """Recalcula a média das avaliações e atualiza o produto."""
        reviews = session.query(Review).filter(Review.product_id == product_id).all()
        avg_rating = sum([r.rating for r in reviews]) / len(reviews) if reviews else 0.0

        session.query(Product).filter(Product.id == product_id).update({"average_rating": avg_rating})
        session.commit()
