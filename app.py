import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Panel de anuncios de vehículos")

df = pd.read_csv("vehicles1_us.csv")
st.dataframe(df)

if st.button("Construir histograma - odometer"):
    fig = px.histogram(df, x="odometer", nbins=45)
    st.plotly_chart(fig, use_container_width=True)

if st.button("Construir dispersion - precio vs odometer"):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
