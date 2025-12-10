import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Product Analysis")

df = pd.read_csv("data/super_shop_data.csv")

product_sales = df.groupby("Product")["Total_Price"].sum().reset_index()

fig = px.bar(product_sales, x="Product", y="Total_Price", color="Total_Price",
             title="Sales by Product", text="Total_Price")
st.plotly_chart(fig)
