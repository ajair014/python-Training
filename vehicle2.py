import streamlit as st

# --- Class Definitions ---
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return "🚗 Car started!"

class ElectricCar(Vehicle):
    def music(self):
        return f"🎶 Brand: {self.brand}, Model: {self.model}\nMusic playing..."

class SmartDevice:
    def wifi(self):
        return f"📶 Brand: {self.brand}, Model: {self.model}\nWiFi connected!"

class SmartCar(ElectricCar, SmartDevice):
    def charge(self):
        return f"⚡ Brand: {self.brand}, Model: {self.model}\nCar is charging..."

class Bike(Vehicle):
    def kickstart(self):
        return f"🏍️ Brand: {self.brand}, Model: {self.model}\nBike started with kickstart!"

class ElectricSmartCar(SmartCar, ElectricCar):
    def auto(self):
        return "🤖 Car is in auto-pilot mode!"

# --- Streamlit UI ---
st.set_page_config(page_title="Vehicle Simulator", page_icon="🚘", layout="centered")

st.title("🚗 Vehicle Feature Simulator")

# User inputs
brand = st.text_input("Enter the brand:")
model = st.text_input("Enter the model:")

choice = st.selectbox(
    "Select an option:",
    ["Select", "Vehicle", "ElectricCar", "SmartDevice", "SmartCar", "Bike", "ElectricSmartCar"]
)

# Create object
esc = ElectricSmartCar(brand, model)

# Action button
if st.button("Show Result"):
    if not brand or not model:
        st.warning("Please enter both brand and model!")
    else:
        if choice == "Vehicle":
            st.success(esc.start())
        elif choice == "ElectricCar":
            st.success(esc.music())
        elif choice == "SmartDevice":
            st.success(esc.wifi())
        elif choice == "SmartCar":
            st.success(esc.charge())
        elif choice == "Bike":
            b = Bike(brand, model)
            st.success(b.kickstart())
        elif choice == "ElectricSmartCar":
            st.success(esc.auto())
        else:
            st.error("Invalid choice, please select an option.")
