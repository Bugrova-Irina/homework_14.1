

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
