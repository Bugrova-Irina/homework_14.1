from baseproduct import BaseProduct
from print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        """строковое отображение продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов"""
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, new_product: dict):
        """
        Принимает на вход параметры товара в словаре и
        возвращает созданный объект класса Product
        """
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Вывод цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Устанавливаем новую цену, если она > 0"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


# product1 = Product(
#     "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
# )
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# print(product1.name)
# print(product1.description)
# print(product1.price)
# print(product1.quantity)
#
# print(product2.name)
# print(product2.description)
# print(product2.price)
# print(product2.quantity)
#
# print(product3.name)
# print(product3.description)
# print(product3.price)
# print(product3.quantity)

# new_product = Product.new_product(
#     {
#         "name": "Samsung Galaxy S23 Ultra",
#         "description": "256GB, Серый цвет, 200MP камера",
#         "price": 180000.0,
#         "quantity": 5,
#     }
# )
# print(new_product.name)
# print(new_product.description)
# print(new_product.price)
# print(new_product.quantity)
#
# new_product.price = 800
# print(new_product.price)
#
# new_product.price = -100
# print(new_product.price)
# new_product.price = 0
# print(new_product.price)
#
# print(str(product1))
# print(str(product2))
# print(str(product3))
#
# print(product1 + product2)
# print(product1 + product3)
# print(product2 + product3)

try:
    product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
except ValueError as e:
    print(
        "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
    )
else:
    print(
        "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
    )
