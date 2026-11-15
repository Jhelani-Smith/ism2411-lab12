
# ISM2411 - Lab 12: CSV Files and Data Processing
# Reflection 1:
#python is better for automating tasks and excel is better for quick manual work.

# Reflection 2:
#becuase it allows for easy addition of new information

import csv
from datetime import datetime

# EXERCISE 2: Read and print raw rows
print("\n--- EXERCISE 2: Raw CSV Rows ---")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header
print("\n--- EXERCISE 3: Skip Header ---")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals
print("\n--- EXERCISE 4: Compute Totals ---")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        product_total = price * quantity
        total_revenue += product_total

        print(
            f"{product}: {quantity} units "
            f"× ${price:.2f} = ${product_total:.2f}"
        )

print(f"Total revenue: ${total_revenue:.2f}")


# EXERCISE 5: Filter and write
print("\n--- EXERCISE 5: Filter and Write ---")

original_count = 0
written_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            product_total = price * quantity

            if product_total > 100:
                writer.writerow([
                    product,
                    price,
                    quantity,
                    f"{product_total:.2f}"
                ])
                written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")
print("Created data/cleaned.csv")


# EXERCISE 6: csv.DictReader
print("\n--- EXERCISE 6: DictReader ---")

dict_total = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        product_total = price * quantity
        dict_total += product_total

        print(f"{product}: ${product_total:.2f}")

print(f"DictReader total revenue: ${dict_total:.2f}")

# csv.reader accesses values using numerical indexes.
# DictReader accesses values using column names, making code easier to read.


# EXERCISE 7: Sales summary by product
print("\n--- EXERCISE 7: Sales Summary ---")

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        product_total = price * quantity

        if product in sales_summary:
            sales_summary[product] += product_total
        else:
            sales_summary[product] = product_total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8: Append mode log
print("\n--- EXERCISE 8: Append Mode Log ---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as file:
    file.write(
        f"{timestamp} | Total Revenue: ${total_revenue:.2f}\n"
    )

print("Sales run successfully added to data/run_log.txt")
