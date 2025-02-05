import pytest


def test_category1_init(category1, product1, product2, product3):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products == [product1, product2, product3]
    assert len(category1.products) == 3
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_category2_init(category2, product4):
    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category2.products == [product4]
    assert len(category2.products) == 1
    assert category2.category_count == 2
    assert category2.product_count == 4


def test_category_products_property(category1, product3, product2, product1):
    assert category1.products == [product1, product2, product3]


def test_category_add_bad_product(category1, bad_product):
    with pytest.raises(TypeError, match="Ожидается объект типа 'Product'"):
        category1.add_product(bad_product)


def test_str_category(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_products_iterator(products_iterator):
    iter(products_iterator)
    assert products_iterator.index == 0
    assert next(products_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(products_iterator).name == "Iphone 15"
    assert next(products_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(products_iterator)


def test_category_middle_prie(category1, category_without_products):
    assert category1.middle_price() == 140333
    assert category_without_products.middle_price() == 0
