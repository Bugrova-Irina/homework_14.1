import pytest

from src.products import Product


def test_product1_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product2_init(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_product3_init(product3):
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_create_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 200MP камера"
    new_product.price = 180000.0
    new_product.quantity = 5


def test_product_update(capsys, product):
    product.price = -100.0
    message = capsys.readouterr()
    message_out = message.out.strip().split("\n")
    assert (
        message_out[0]
        == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )
    assert message_out[1] == "Цена не должна быть нулевая или отрицательная"

    product.price = 800
    assert product.price == 800


def test_product_price_property(product3):
    assert product3.price == 31000.0


def test_str_product(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product1, product2):
    assert product1 + product2 == 2580000.0


def test_product_with_invalid_quantity():
    """Тест на создание товара с нулевым количеством"""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
