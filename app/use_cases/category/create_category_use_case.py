from sqlalchemy.orm import Session
from app.database.models import Category as CategoryModel
from app.schemas.category import Category

class CreateCategoryUseCase:
    
    def __init__(self,db_session: Session):
        self.db_session = db_session
        
    def add_category(self, category: Category):
        data = CategoryModel(**category.dict())
        self.db_session.add(data)
        self.db_session.commit()