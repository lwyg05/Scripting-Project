
def create_product(product_id, name, category, price, quantity):

    return {
        "id": str(product_id),
        "name": str(name),
        "category": str(category),
        "price": float(price),
        "quantity": int(quantity)
    }


def display_product(product):

    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Category: {product['category']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Quantity: {product['quantity']}")
    print("-" * 40)
