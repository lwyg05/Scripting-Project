import csv
from datetime import date


def recordsale(inventory, transactions, productid, quantity):
    """Find product, check stock, create transaction, reduce stock."""

    
    product = None
    for item in inventory:
        if item["id"] == productid:
            product = item
            break

    if product is None:
        print(f"Error: Product ID '{productid}' not found.")
        return False

    if product["quantity"] < quantity:
        print(f"Error: Insufficient stock. Available: {product['quantity']}, Requested: {quantity}")
        return False

    transaction_id = "T" + str(len(transactions) + 1).zfill(3)

   
    total_amount = product["price"] * quantity

 
    transaction = {
        "transactionid": transaction_id,
        "productid": productid,
        "quantitysold": int(quantity),
        "unitprice": float(product["price"]),
        "totalamount": float(total_amount),
        "date": str(date.today())
    }


    transactions.append(transaction)

    product["quantity"] -= quantity

    print(f"Sale recorded successfully! Transaction ID: {transaction_id}")
    print(f"  Product : {product['name']}")
    print(f"  Quantity: {quantity}")
    print(f"  Total   : ${total_amount:.2f}")
    print(f"  Stock left: {product['quantity']}")
    return True


def viewtransactions(transactions):
    """Display all recorded transactions."""

    if not transactions:
        print("No transactions recorded yet.")
        return

    print("\n=== Transaction History ===")
    for t in transactions:
        print(f"Transaction ID : {t['transactionid']}")
        print(f"Product ID     : {t['productid']}")
        print(f"Quantity Sold  : {t['quantitysold']}")
        print(f"Unit Price     : ${t['unitprice']:.2f}")
        print(f"Total Amount   : ${t['totalamount']:.2f}")
        print(f"Date           : {t['date']}")
        print("-" * 40)


def savetransactionstocsv(transactions, filename):
    """Save all transactions to a CSV file."""

    if not transactions:
        print("No transactions to save.")
        return False

    try:
        fieldnames = ["transactionid", "productid", "quantitysold", "unitprice", "totalamount", "date"]
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for t in transactions:
                writer.writerow(t)
        print(f"Transactions saved to '{filename}' successfully.")
        return True
    except Exception as e:
        print(f"Error saving transactions: {e}")
        return False


def loadtransactionsfromcsv(filename):
    """Load transactions from a CSV file and return as a list of dicts."""

    transactions = []
    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                row["quantitysold"] = int(row["quantitysold"])
                row["unitprice"] = float(row["unitprice"])
                row["totalamount"] = float(row["totalamount"])
                transactions.append(row)
        print(f"Loaded {len(transactions)} transactions from '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error loading transactions: {e}")

    return transactions
