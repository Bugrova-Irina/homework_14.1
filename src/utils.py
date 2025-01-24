import json
import os

from products import Product
from category import Category


def read_json(path: str) -> dict:
    """Чтение данных из json-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def create_objects_from_json(data):
    """Создание объектов класса из json-данных"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    raw_data = read_json("../homework_14.1/data/products.json")
    categories_data = create_objects_from_json(raw_data)

    # print(categories_data[0].name)
    # print(categories_data[0].products)
    # print(raw_data)
    print(categories_data)
