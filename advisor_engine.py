def generate_advice(income, expenses, savings_goal):
    savings = income - sum(expenses.values())
    advice = []

    if savings < savings_goal:
        advice.append("You're saving less than your goal. Consider cutting back on variable expenses.")

    if expenses["Food"] > 0.3 * income:
        advice.append("High food expenses detected. Cooking at home might help save money.")

    if savings > 0.2 * income:
        advice.append("Great job! You’re saving over 20% of your income. Consider investing the surplus.")

    if sum(expenses.values()) > 0.8 * income:
        advice.append("You're spending over 80% of your income. Try to reduce non-essential costs.")

    return advice
