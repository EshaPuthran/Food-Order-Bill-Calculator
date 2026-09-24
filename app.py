# ========================================
#       FOOD ORDER & BILL CALCULATOR
# ========================================

print("========================================")
print("        FOOD ORDER & BILL CALCULATOR")
print("========================================")

# Get customer name
name = input("Enter customer name: ")

# Display menu
print("\n----------- MENU -----------")
print("1. Burger       - Rs. 120")
print("2. Pizza        - Rs. 250")
print("3. Sandwich     - Rs. 100")
print("4. French Fries - Rs. 80")
print("----------------------------")

# Get customer's choice
choice = int(input("Enter your choice (1-4): "))

# Get quantity
quantity = int(input("Enter quantity: "))

# Determine food item and price
if choice == 1:
    item = "Burger"
    price = 120

elif choice == 2:
    item = "Pizza"
    price = 250

elif choice == 3:
    item = "Sandwich"
    price = 100

elif choice == 4:
    item = "French Fries"
    price = 80

else:
    item = "Invalid Item"
    price = 0

# Calculate total
total = price * quantity

# Calculate discount
if total >= 500:
    discount = total * 0.10

elif total >= 300:
    discount = total * 0.05

else:
    discount = 0

# Calculate final bill
final_bill = total - discount

# Display bill
print("\n========================================")
print("              YOUR BILL")
print("========================================")

print("Customer Name :", name)
print("Food Item     :", item)
print("Quantity      :", quantity)
print("Price         : Rs.", price)
print("----------------------------------------")
print("Total Amount  : Rs.", total)
print("Discount      : Rs.", discount)
print("Final Bill    : Rs.", final_bill)

print("========================================")
print("       Thank you for ordering!")
print("========================================")