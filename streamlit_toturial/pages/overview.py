import streamlit as st
import pandas as pd

st.title("📄 Overview")

df = pd.read_csv("data/super_shop_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"{df['Total_Price'].sum()} ৳")
col2.metric("Total Quantity", df["Quantity"].sum())
col3.metric("Average Unit Price", round(df["Unit_Price"].mean(),2))
