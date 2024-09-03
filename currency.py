import streamlit as st

st.title("Currency Converter")

# User inputs
amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f")
exchange_rate = 0.85  # Example exchange rate: 1 USD = 0.85 EUR

# Convert the currency
converted_amount = amount * exchange_rate

# Display the result
st.write(f"{amount} USD is equal to {converted_amount:.2f} EUR")
