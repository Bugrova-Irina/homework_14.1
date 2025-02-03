import pytest


def test_lawngrass_init(grass1):
    """Проверяем инициализацию класса Газонная трава"""
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_add(grass1, grass2):
    """Проверяем сложение объектов одного класса"""
    assert grass1.price * grass1.quantity + grass2.price * grass2.quantity == 16750.0


def test_lawngrass_add_error(grass1):
    """Проверяем сложение объектов разных классов"""
    with pytest.raises(TypeError):
        result = grass1 + 1
