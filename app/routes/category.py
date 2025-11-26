from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.routes.deps import get_database_session
from app.schemas.category import Category
from app.use_cases.category.create_category_use_case import CreateCategoryUseCase

router = APIRouter(prefix="/category", tags=['category'])

@router.post('/add')
def add_category(
    category: Category,
    db_session: Session = Depends(get_database_session)
):
    uc = CreateCategoryUseCase(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)