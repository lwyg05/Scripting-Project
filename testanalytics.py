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
from inventory import add_product

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

print("\n=== Testing transactions.py ===\n")
inventory = []
transactions_list = []

p1 = create_product("P001", "Laptop", "Electronics", 2500, 10)
p2 = create_product("P002", "Mouse", "Electronics", 50, 3)
add_product(inventory, p1)
add_product(inventory, p2)

print("--- Recording a valid sale ---")
recordsale(inventory, transactions_list, "P001", 2)
for item in inventory:
    if item["id"] == "P001":
        print(f"P001 stock after sale: {item['quantity']}")

print("\n--- Attempting sale with insufficient stock ---")
recordsale(inventory, transactions_list, "P002", 10)

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
print("Mean sale total:", calculatemean(totals))
