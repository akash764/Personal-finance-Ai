def calculate_totals(income, expenses):
    total_expense = sum(expenses.values())
    savings = income - total_expense
    return total_expense, savings
