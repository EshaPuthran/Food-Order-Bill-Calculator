import streamlit as st

# Page title
st.title(" Food Order & Bill Calculator")
st.write("Welcome! Calculate your food order bill easily.")

# Customer name
name = st.text_input("Enter your name")

# Menu
st.subheader(" Menu")

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Sandwich": 100,
    "French Fries": 80
}

# Display menu
for item, price in menu.items():
    st.write(item, "- ₹", price)

# Select food item
item = st.selectbox(
    "Select your food item",
    ["Burger", "Pizza", "Sandwich", "French Fries"]
)

# Quantity
quantity = st.number_input(
    "Enter quantity",
    min_value=1,
    value=1
)

# Get price
price = menu[item]

# Calculate total
total = price * quantity

# Discount
if total >= 500:
    discount = total * 0.10
elif total >= 300:
    discount = total * 0.05
else:
    discount = 0

# Final bill
final_bill = total - discount

# Button
if st.button("Calculate Bill"):

    if name == "":
        st.warning("Please enter your name.")

    else:
        st.success("Bill calculated successfully!")

        st.subheader("Your Bill")

        st.write("**Customer Name:**", name)
        st.write("**Food Item:**", item)
        st.write("**Quantity:**", quantity)
        st.write("**Price per item:** ₹", price)

        st.write("---")

        st.write("**Total Amount:** ₹", total)
        st.write("**Discount:** ₹", discount)
        st.write("### Final Bill: ₹", final_bill)

        st.write("Thank you for ordering! ")