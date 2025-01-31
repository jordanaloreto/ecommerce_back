from app.repositories.review_repository import ReviewRepository
from app.models.review_model import ReviewCreate

class ReviewService:
    def __init__(self):
        self.repository = ReviewRepository()  # Instância do repositório

    # Retorna todas as avaliações
    def get_all_reviews(self):
        return self.repository.get_all()
    
    # Retorna avaliações de um produto específico
    def get_reviews_by_product(self, product_id: int):
        return self.repository.get_by_product(product_id)

    # Retorna uma avaliação pelo ID
    def get_review_by_id(self, review_id: int):
        return self.repository.get_by_id(review_id)

    # Cria uma nova avaliação e atualiza a média de notas do produto
    def create_review(self, review: ReviewCreate):
        return self.repository.create(review)
    
    # Atualiza uma avaliação
    def update_review(self, review_id: int, review_data: ReviewCreate):
        return self.repository.update(review_id, review_data)

    # Remove uma avaliação e recalcula a média do produto
    def delete_review(self, review_id: int):
        return self.repository.delete(review_id)
