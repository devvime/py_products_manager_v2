import pytest
from app.schemas.category import Category

def test_category_schema():
    category = Category(
        name="Car",
        slug="cars"
    )
    
    assert category.dict() == {
        'name': 'Car',
        'slug': 'cars'
    }
    
    
def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        Category = Category(
            name="Car",
            slug="ball"
        )
    
    with pytest.raises(ValueError):
        Category = Category(
            name="Car",
            slug="$rgf ofo"
        )