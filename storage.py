import pandas as pd

if st.button("Save My Data"):
    df = pd.DataFrame([{
        "Income": income,
        "Fixed": fixed_expense,
        "Food": food_expense,
        "Travel": travel_expense,
        "Other": other_expense,
        "Savings": actual_savings
    }])
    df.to_csv("user_finance_data.csv", mode='a', index=False)
    st.success("Saved successfully!")
