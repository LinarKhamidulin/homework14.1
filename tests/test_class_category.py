import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def product1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return product1


@pytest.fixture
def product2():
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product2


@pytest.fixture
def category(product1, product2):
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2])
    return category1


def test_init(category):
    assert Category.name == "Смартфоны"
    assert Category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(Category.products) == 2
    assert Category.product_count == 1
    assert Category.category_count == 2
