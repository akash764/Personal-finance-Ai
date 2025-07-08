def generate_advice(income, total_expense, savings_goal):
    savings = income - total_expense
    advice = []

    if savings < savings_goal:
        advice.append("You're saving less than your goal. Reduce discretionary expenses.")
    if food_expense > 0.3 * income:
        advice.append("Food expenses exceed 30% of income. Consider cooking at home.")
    if actual_savings > 0.2 * income:
        advice.append("Great! You're saving more than 20%. Consider investing in SIP or FD.")
    if total_expense > 0.8 * income:
        advice.append("You're spending more than 80% of your income. Try to cut non-essential costs.")
    
    return advice

st.subheader("🧠 Smart Advice")
for tip in generate_advice(income, total_expense, savings_goal):
    st.info(tip)
