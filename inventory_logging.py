# Inventory Logging at Big Wig Electronics

# Keyboard Input
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity received: "))
supplier = input("Enter supplier name: ")
cost_per_unit = float(input("Enter cost per unit (R): "))

# Calculate Total Cost
total_cost = quantity * cost_per_unit

# Check for Large Order
note = ""
if total_cost > 500:
    note = " (Large Order)"

# Display Output
print("\nInventory Entry")
print("Product:", product_name)
print("Quantity:", quantity)
print("Supplier:", supplier)
print("Total Cost: R{:.2f}".format(total_cost))

# Display binary representation of quantity
print("Quantity in Binary:", bin(quantity))

# Format entry for file
entry = (
    f"Product: {product_name}, "
    f"Quantity: {quantity}, "
    f"Supplier: {supplier}, "
    f"Total Cost: R{total_cost:.2f}"
    f"{note}"
)

# Save to file without overwriting
file = open("inventory_log.txt", "a")
file.write(entry + "\n")
file.close()

print("Entry saved successfully.")