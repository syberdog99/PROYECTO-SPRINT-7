import streamlit as st 
import pandas as pd 
import plotly.graph_objects as go
car_data = pd.read_csv("vehicles_us.csv")
st.header("Analisis de anuncios de venta de coches")
hist_button = st.button("construir histograma")
if hist_button:
    st.write("Creacion de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribucion del Odometro")
    st.plotly_chart(fig, use_container_width=True)
disp_button = st.button("construir grafico de dispersion")
if disp_button:
    st.write("Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches")
    fig = go.Figure(data=[go.Scatter(x=car_data["odometer"], y=car_data["price"], mode="markers")])
    fig.update_layout(title_text="Relacion entre Odometro y Precio")
    st.plotly_chart(fig, use_container_width=True)

    fig.show()
    