from pony.orm import db_session

from models import Orders, Products


class OrderRepository:
    def __init__(self):
        self.__model = Orders

    @db_session
    def add_order(self, order_id, product_id, quantity):
        self.__model(order_id=order_id, product_id=Products[product_id], quantity=quantity)

# if __name__ == '__main__':
# OrderRepository().add_order(1, 3, 4)
# OrderRepository().add_order(1, 2, 4)
# OrderRepository().add_order(1, 3, 4)
# OrderRepository().add_order(2, 5, 1)
# OrderRepository().add_order(2, 3, 2)
# OrderRepository().add_order(3, 4, 1)
# OrderRepository().add_order(3, 2, 10)
# OrderRepository().add_order(3, 5, 2)
# OrderRepository().add_order(4, 1, 2)
# OrderRepository().add_order(4, 2, 3)
# OrderRepository().add_order(5, 1, 3)
# OrderRepository().add_order(5, 5, 1)
# OrderRepository().add_order(5, 4, 1)
# OrderRepository().get_qty_sale_product()