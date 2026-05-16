import analytics
import transactions
from analytics import (
    calculatemean, calculatemedian, calculatemode,
    calculatevariance, calculatestddeviation,
    calculatecorrelation, calculatemovingaverage,
    getsalestotals, getquantitiessold
)
from transactions import recordsale, viewtransactions, savetransactionstocsv, loadtransactionsfromcsv
from product import create_product
from inventory import add_product, remove_product, update_product, save_inventory_to_csv, load_inventory_from_csv
from reports import inventory_summary, low_stock_report, sales_summary, full_report

# ── Analytics tests 
print("=== Testing analytics.py ===\n")
print("Mean of [10, 20, 30]:", calculatemean([10, 20, 30]))
print("Median of [1, 3, 2]:", calculatemedian([1, 3, 2]))
print("Median of [1, 2, 3, 4]:", calculatemedian([1, 2, 3, 4]))
print("Mode of [1, 2, 2, 3]:", calculatemode([1, 2, 2, 3]))
print("Variance of [2,4,4,4,5,5,7,9]:", calculatevariance([2,4,4,4,5,5,7,9]))
print("Std Dev of [2,4,4,4,5,5,7,9]:", calculatestddeviation([2,4,4,4,5,5,7,9]))
print("Correlation of [1,2,3] and [4,5,6]:", calculatecorrelation([1,2,3],[4,5,6]))
print("Moving Average [1,2,3,4,5] window=3:", calculatemovingaverage([1,2,3,4,5], 3))
print("Empty list mean:", calculatemean([]))

# ── Inventory tests 
print("\n=== Testing inventory.py ===\n")
inventory = []
transactions_list = []

p1 = create_product("P001", "Laptop", "Electronics", 2500, 10)
p2 = create_product("P002", "Mouse", "Electronics", 50, 3)
p3 = create_product("P003", "Keyboard", "Electronics", 100, 2)
add_product(inventory, p1)
add_product(inventory, p2)
add_product(inventory, p3)

print("--- Duplicate product ID ---")
add_product(inventory, p1)

print("\n--- Update product price ---")
update_product(inventory, "P001", "price", 3000)

print("\n--- Update invalid field ---")
update_product(inventory, "P001", "color", "red")

print("\n--- Remove product ---")
remove_product(inventory, "P002")

print("\n--- Remove product that doesn't exist ---")
remove_product(inventory, "P999")

print("\n--- Save inventory to CSV ---")
save_inventory_to_csv(inventory, "inventory.csv")

print("\n--- Load inventory from CSV ---")
loaded_inventory = load_inventory_from_csv("inventory.csv")
print(f"Loaded {len(loaded_inventory)} product(s).")

# ── Transactions tests 
print("\n=== Testing transactions.py ===\n")

print("--- Recording a valid sale ---")
recordsale(inventory, transactions_list, "P001", 2)
for item in inventory:
    if item["id"] == "P001":
        print(f"P001 stock after sale: {item['quantity']}")

print("\n--- Attempting sale with insufficient stock ---")
recordsale(inventory, transactions_list, "P003", 10)

print("\n--- Attempting sale with invalid product ID ---")
recordsale(inventory, transactions_list, "P999", 1)

print()
viewtransactions(transactions_list)

print("--- Saving to CSV ---")
savetransactionstocsv(transactions_list, "transactions.csv")

print("--- Loading from CSV ---")
loaded = loadtransactionsfromcsv("transactions.csv")
print(f"Loaded {len(loaded)} transaction(s).")
print("Types check — quantitysold is int:", isinstance(loaded[0]["quantitysold"], int))
print("Types check — totalamount is float:", isinstance(loaded[0]["totalamount"], float))

print("\n--- Helper functions ---")
totals = getsalestotals(transactions_list)
qtys = getquantitiessold(transactions_list)
print("Sale totals:", totals)
print("Quantities sold:", qtys)
