import json
import os
import streamlit as st

DATA_FILE = "bank_data.json"

# ---------- Save data to JSON ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Load existing data (if available) ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                st.warning("Warning: JSON file was empty or corrupted. Starting fresh.")
                return {}
    else:
        return {}

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Bank Account Manager", page_icon="🏦")
st.title("🏦 Bank Account Manager")
st.write("Easily **Create**, **View**, **Update**, and **Delete** bank accounts using this simple CRUD app.")

# Load existing data
data = load_data()

# ---------- Menu ----------
menu = st.sidebar.radio("Select an Operation", ["Create Account", "Display All Accounts", "Update Account", "Delete Account"])

# ---------- CREATE ----------
if menu == "Create Account":
    st.subheader("➕ Create a New Account")
    name = st.text_input("Enter account holder name")
    pin = st.text_input("Enter 4-digit PIN", type="password", max_chars=4)
    balance = st.number_input("Enter initial balance", min_value=0.0)

    if st.button("Create Account"):
        if not name or not pin:
            st.error("Please fill all fields!")
        elif name in data:
            st.warning(f"Account for '{name}' already exists!")
        else:
            data[name] = {
                "account_holder": name,
                "pin": pin,
                "balance": balance
            }
            save_data(data)
            st.success(f"Account for '{name}' created successfully!")

# ---------- DISPLAY ----------
elif menu == "Display All Accounts":
    st.subheader("📋 All Bank Accounts")

    if not data:
        st.info("No accounts found.")
    else:
        for account in data.values():
            with st.expander(f"Account: {account['account_holder']}"):
                st.write(f"**PIN:** {account['pin']}")
                st.write(f"**Balance:** ₹{account['balance']}")

# ---------- UPDATE ----------
elif menu == "Update Account":
    st.subheader("✏️ Update Account Details")

    if not data:
        st.info("No accounts available to update.")
    else:
        selected_name = st.selectbox("Select account to update", list(data.keys()))
        update_choice = st.radio("What would you like to update?", ["PIN", "Balance"])

        if update_choice == "PIN":
            new_pin = st.text_input("Enter new 4-digit PIN", type="password", max_chars=4)
            if st.button("Update PIN"):
                if new_pin:
                    data[selected_name]['pin'] = new_pin
                    save_data(data)
                    st.success(f"PIN updated for '{selected_name}' successfully!")
                else:
                    st.error("Please enter a valid PIN.")
        else:
            new_balance = st.number_input("Enter new balance", min_value=0.0)
            if st.button("Update Balance"):
                data[selected_name]['balance'] = new_balance
                save_data(data)
                st.success(f"Balance updated for '{selected_name}' successfully!")

# ---------- DELETE ----------
elif menu == "Delete Account":
    st.subheader("🗑️ Delete Account")

    if not data:
        st.info("No accounts available to delete.")
    else:
        selected_name = st.selectbox("Select account to delete", list(data.keys()))
        confirm = st.checkbox(f"Yes, delete account '{selected_name}'")

        if st.button("Delete Account"):
            if confirm:
                del data[selected_name]
                save_data(data)
                st.success(f"Account '{selected_name}' deleted successfully!")
            else:
                st.warning("Please confirm deletion before proceeding.")

    