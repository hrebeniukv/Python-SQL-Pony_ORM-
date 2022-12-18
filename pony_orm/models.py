from pony.orm import Database, PrimaryKey, Required, Set, set_sql_debug

db = Database()
db.bind('postgres', user='postgres', password='1280', host='127.0.0.1', database='store')


class Products(db.Entity):
    _table_ = "products"
    id = PrimaryKey(int, auto=True)
    name = Required(str, 30, unique=True)
    price = Required(float)
    orders = Set("Orders")


class Orders(db.Entity):
    _table_ = "orders"
    id = PrimaryKey(int, auto=True)
    order_id = Required(int)
    quantity = Required(int)
    product_id = Required(Products)


set_sql_debug(False)
db.generate_mapping(create_tables=True)
