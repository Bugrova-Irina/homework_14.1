import pytest


def test_smartphone_init(smartphone1):
    """Проверяем инициализацию класса Смартфон"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

def test_smartphone_add(smartphone1, smartphone2):
    """Проверяем сложение объектов одного класса"""
    assert smartphone1.price * smartphone1.quantity + smartphone2.price * smartphone2.quantity == 2580000.0


def test_smartphone_add_error(smartphone1):
    """Проверяем сложение объектов разных классов"""
    with pytest.raises(TypeError):
        result = smartphone1 + 1
