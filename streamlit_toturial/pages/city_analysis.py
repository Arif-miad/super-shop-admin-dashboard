import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏙️ City Analysis")

df = pd.read_csv("data/super_shop_data.csv")

city_sales = df.groupby("City")["Total_Price"].sum().reset_index()

fig = px.pie(city_sales, names="City", values="Total_Price", title="Sales Share by City")
st.plotly_chart(fig)
