import streamlit as st

# --- App title ---
st.set_page_config(page_title="🧮 Calculator App", layout="centered")
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations easily!")

# --- Input fields ---
num1 = st.number_input("Enter first number:", step=1.0, format="%.6f")
num2 = st.number_input("Enter second number:", step=1.0, format="%.6f")

# --- Operation selection ---
operation = st.selectbox(
    "Select Operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# --- Calculate button ---
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Cannot divide by zero!")
                result = None
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
