import streamlit as st
from advisor_engine import generate_advice
from finance_calculator import calculate_totals
from visualizer import show_expense_pie
from storage import save_user_data

st.set_page_config(page_title="AI Personal Finance Advisor", page_icon="💰")
st.title("💰 AI Personal Finance Advisor")

st.sidebar.header("Enter Your Monthly Data")

income = st.sidebar.number_input("Enter your Monthly Income (₹)", min_value=0)
fixed_expense = st.sidebar.number_input("Fixed Expenses (Rent, EMIs)", min_value=0)
food_expense = st.sidebar.number_input("Food & Groceries", min_value=0)
travel_expense = st.sidebar.number_input("Travel & Transport", min_value=0)
other_expense = st.sidebar.number_input("Other Expenses", min_value=0)
savings_goal = st.sidebar.number_input("Desired Monthly Savings", min_value=0)

if income > 0:
    expenses = {
        "Fixed": fixed_expense,
        "Food": food_expense,
        "Travel": travel_expense,
        "Other": other_expense
    }

    total_expense, actual_savings = calculate_totals(income, expenses)

    st.subheader("📊 Summary")
    st.write(f"**Total Expense:** ₹{total_expense}")
    st.write(f"**Actual Savings:** ₹{actual_savings}")

    st.subheader("🧠 AI Advice")
    advice_list = generate_advice(income, expenses, savings_goal)
    if advice_list:
        for tip in advice_list:
            st.info(tip)
    else:
        st.success("You’re doing great! Your finances look good.")

    st.subheader("📈 Expense Breakdown")
    show_expense_pie(expenses)

    if st.button("Save My Data"):
        save_user_data(income, expenses, actual_savings)
        st.success("✅ Data saved successfully!")

else:
    st.warning("👈 Please enter your income and expenses to get advice.")
