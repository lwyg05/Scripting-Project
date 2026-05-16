%%writefile reports.py

def inventory_summary(inventory):

    print("\n=== Inventory Summary ===")

    if not inventory:
        print("Inventory is empty.")
        return

    total_products = len(inventory)
    total_quantity = sum(product["quantity"] for product in inventory)
    total_value = sum(product["price"] * product["quantity"] for product in inventory)

    print(f"Total Products: {total_products}")
    print(f"Total Quantity: {total_quantity}")
    print(f"Total Inventory Value: ${total_value:.2f}")


def low_stock_report(inventory, limit=5):

    print("\n=== Low Stock Report ===")

    found = False

    for product in inventory:
        if product["quantity"] <= limit:
            print(f"{product['name']} | Stock: {product['quantity']}")
            found = True

    if not found:
        print("No low stock products.")


def sales_summary(transactions):

    print("\n=== Sales Summary ===")

    if not transactions:
        print("No sales transactions.")
        return

    total_sales = sum(t["totalamount"] for t in transactions)
    total_items = sum(t["quantitysold"] for t in transactions)

    print(f"Total Sales Amount: ${total_sales:.2f}")
    print(f"Total Items Sold: {total_items}")
    print(f"Total Transactions: {len(transactions)}")


def full_report(inventory, transactions):

    print("\n========== FULL REPORT ==========")

    inventory_summary(inventory)
    low_stock_report(inventory)
    sales_summary(transactions)

    print("=================================")
