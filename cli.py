%%writefile cli.py

from product import create_product
from inventory import add_product, list_all_products
from transactions import recordsale, viewtransactions
from reports import inventory_summary, low_stock_report, sales_summary, full_report


def start_menu():
    inventory = []
    transactions = []

    while True:
        print("\n========== Inventory Management & Sales Analytics System ==========")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Record Sale")
        print("4. View Transactions")
        print("5. Inventory Summary")
        print("6. Low Stock Report")
        print("7. Sales Summary")
        print("8. Full Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            product = create_product(product_id, name, category, price, quantity)
            add_product(inventory, product)

        elif choice == "2":
            list_all_products(inventory)

        elif choice == "3":
            product_id = input("Enter product ID to sell: ")
            quantity = int(input("Enter quantity sold: "))
            recordsale(inventory, transactions, product_id, quantity)

        elif choice == "4":
            viewtransactions(transactions)

        elif choice == "5":
            inventory_summary(inventory)

        elif choice == "6":
            low_stock_report(inventory)

        elif choice == "7":
            sales_summary(transactions)

        elif choice == "8":
            full_report(inventory, transactions)

        elif choice == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
