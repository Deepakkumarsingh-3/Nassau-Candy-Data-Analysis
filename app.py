import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🍬 Nassau Candy Sales & Operations Dashboard")

# Load data
df = pd.read_csv("Cleaned_Nassau_Candy_Data.csv")

# KPI Metrics at a glance
total_sales = df['Sales'].sum()
total_profit = df['Gross Profit'].sum()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Gross Profit", f"${total_profit:,.2f}")

# Show Factory Insights Table
st.subheader("Factory Performance Breakdown")
factory_perf = df.groupby('Factory')[['Sales', 'Gross Profit']].sum().reset_index()
st.dataframe(factory_perf)

# Render your Top Products Chart dynamically
st.subheader("Top 5 Most Profitable Products")
top_products = df.groupby('Product Name')['Gross Profit'].sum().nlargest(5).reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(top_products['Product Name'], top_products['Gross Profit'], color='skyblue')
ax.set_xlabel('Gross Profit ($)')
ax.invert_yaxis()
st.pyplot(fig)