from products import Product, product1, product2, product3
from lawngrass import grass1, grass2
from smartphone import smartphone1, smartphone2, smartphone3


class Category:
    """Класс Category"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if self.__products else 0

    def __str__(self):
        """строковое отображение категории"""
        sum_quantity = 0
        for product in self.products:
            sum_quantity += int(product.quantity)
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    @property
    def products(self):
        """Вывод продуктов"""
        return self.__products

    def add_product(self, product: Product):
        """добавление товаров в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Ожидается объект типа 'Product'")
        else:
            self.__products.append(product)
            Category.product_count += 1
            print(f"{str(product)}\n")

    @classmethod
    def reset_counters(cls):
        """Сброс счетчиков"""
        cls.category_count = 0
        cls.product_count = 0


# if __name__ == "__main__":
category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

print(category1.products)
product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
category1.add_product(product4)
print(category1.products)
print(category1.product_count)

# product5 = ('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
# category1.add_product(product5)
# print(category1.products)

print(str(category1))

# print(category1.products)

category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

category_smartphones.add_product(smartphone3)

print(category_smartphones.products)

print(Category.product_count)

try:
    category_smartphones.add_product("Not a product")
except TypeError:
    print("Возникла ошибка TypeError при добавлении не продукта")
else:
    print("Не возникла ошибка TypeError при добавлении не продукта")