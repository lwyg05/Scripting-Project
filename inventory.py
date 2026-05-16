import csv
from product import display_product


def add_product(inventory, product):
    if search_product(inventory, product["id"]) is not None:
        print("Error: Product ID already exists.")
        return False

    inventory.append(product)
    print("Product added successfully.")
    return True

def remove_product(inventory, product_id):

    product = search_product(inventory, product_id)

    if product is None:
        print("Error: Product not found.")
        return False

    inventory.remove(product)
    print("Product removed successfully.")
    return True

def search_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None

def update_product(inventory, product_id, field, new_value):

    product = search_product(inventory, product_id)

    if product is None:
        print("Error: Product not found.")
        return False

    if field not in product:
        print("Error: Invalid field.")
        return False

    if field == "price":
        product[field] = float(new_value)
    elif field == "quantity":
        product[field] = int(new_value)
    elif field == "id":
        print("Error: Product ID should not be changed.")
        return False
    else:
        product[field] = str(new_value)

    print("Product updated successfully.")
    return True


def list_all_products(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n=== Inventory Products ===")
    for product in inventory:
        display_product(product)

def save_inventory_to_csv(inventory, filename):

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "name", "category", "price", "quantity"]
        )
        writer.writeheader()
        writer.writerows(inventory)

    print(f"Inventory saved to {filename}")


def load_inventory_from_csv(filename):

    inventory = []

    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["price"] = float(row["price"])
                row["quantity"] = int(row["quantity"])
                inventory.append(row)

        print(f"Inventory loaded from {filename}")

    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty inventory.")

    return inventory
