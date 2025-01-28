from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products = dao.list_products()
    result = []
    for product in products:
        result.append(Product.load(product))
    
    return result



def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))

def get_products_paginated(page, products_per_page):
    try:
        # Calculate offset for pagination
        offset = (page - 1) * products_per_page

        # Optimized query with placeholders for SQL injection prevention
        query = "SELECT * FROM products LIMIT %s OFFSET %s"
        return execute_query(query, [products_per_page, offset])

    except Exception as e:
        print(f"Error in get_products_paginated: {e}")
        return []

def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)


