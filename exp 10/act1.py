"""
Created on Tue May 12 09:12:06 2026

@author:Pradnya jadhav
"""

import streamlit as st

st.set_page_config(page_title="Grocery Bill Calculator", page_icon="🛒")

st.title("🛒 Grocery Bill Calculator")

st.write("Enter grocery item details below:")

# Input fields
item_name = st.text_input("Item Name")
quantity = st.number_input("Quantity", min_value=1, step=1)
price = st.number_input("Price per Item", min_value=0.0, step=0.5)

# Session state for storing items
if "cart" not in st.session_state:
    st.session_state.cart = []

# Add item button
if st.button("Add Item"):
    total = quantity * price
    st.session_state.cart.append({
        "Item": item_name,
        "Quantity": quantity,
        "Price": price,
        "Total": total
    })
    st.success(f"{item_name} added successfully!")

# Display bill
if st.session_state.cart:
    st.subheader("🧾 Grocery Bill")

    grand_total = 0

    for item in st.session_state.cart:
        st.write(
            f"{item['Item']} | Qty: {item['Quantity']} | "
            f"Price: ₹{item['Price']} | Total: ₹{item['Total']}"
        )
        grand_total += item['Total']

    st.markdown("---")
    st.subheader(f"Grand Total: ₹{grand_total}")

# Clear bill button
if st.button("Clear Bill"):
    st.session_state.cart = []
    st.warning("Bill Cleared!")
