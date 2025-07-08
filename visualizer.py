import matplotlib.pyplot as plt

labels = ['Fixed', 'Food', 'Travel', 'Other']
sizes = [fixed_expense, food_expense, travel_expense, other_expense]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
st.pyplot(fig)
