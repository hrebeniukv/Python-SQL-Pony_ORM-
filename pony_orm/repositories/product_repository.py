from pony.orm import db_session

from models import Products
from utilities.sell_report import SellReport


class ProductRepository:
    def __init__(self):
        self.__model = Products

    @db_session
    def add_product(self, name, price):
        self.__model(name=name, price=price)

    @db_session
    def get_sale_information(self, name=None):
        if name:
            products = self.__model.select(lambda product: product.name == name)
        else:
            products = self.__model.select()
        products_list = []
        for product in products:
            if product.orders:
                qty = sum(j.quantity for j in product.orders)
                data = {'name': product.name, 'price': product.price, 'sold_quantity': qty,
                        'total': product.price * qty}
                products_list.append(SellReport(**data))
        return products_list


if __name__ == '__main__':
    # ProductRepository().add_product(name="knife", price=13.40)
    # ProductRepository().add_product(name="fork", price=4.36)
    # ProductRepository().add_product(name="spoon", price=5.30)
    # ProductRepository().add_product(name="pan", price=23.73)
    # ProductRepository().add_product(name="pot", price=18.55)
    sale_products_all_product = [print(i) for i in ProductRepository().get_sale_information()]
    sale_product_by_name = [print(i) for i in ProductRepository().get_sale_information('spoon')]
