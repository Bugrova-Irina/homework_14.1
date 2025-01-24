from products import Product, product1, product2, product3


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

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
        print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")

    @classmethod
    def reset_counters(cls):
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
