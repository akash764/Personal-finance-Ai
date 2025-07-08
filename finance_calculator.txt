total_expense = fixed_expense + food_expense + travel_expense + other_expense
actual_savings = income - total_expense

st.subheader("📈 Summary")
st.write(f"**Total Expense:** ₹{total_expense}")
st.write(f"**Actual Savings:** ₹{actual_savings}")
