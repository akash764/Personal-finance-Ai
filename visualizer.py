import matplotlib.pyplot as plt
import streamlit as st

def show_expense_pie(expenses):
    labels = list(expenses.keys())
    sizes = list(expenses.values())
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures pie chart is circular

    st.pyplot(fig)
