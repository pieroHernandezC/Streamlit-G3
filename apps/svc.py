import streamlit as st
from sklearn.svm import SVC
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def app():
    st.title("Modelo SVC")
    st.title("Predicción de tendencia de acciones del Mes usando SVC")

    start = st.date_input("Inicio (Start)", value=pd.to_datetime("2022-12-01"))
    end = st.date_input("Fin (End)", value=pd.to_datetime("today"))
    user_input = st.text_input("Introducir cotización bursátil", "AVGO")

    df = yf.download(user_input, start, end)
    df.index = df.index.strftime('%Y-%m-%d')
    df.reset_index(inplace=True)

    st.subheader("Datos del Diciembre - 2022")
    st.write(df)
    st.subheader("Descripción de la dataset")
    st.write(df.describe())

    st.subheader("Closing Price vs Time")
    fig = plt.figure(figsize=(12, 6))
    plt.plot(df.Close)
    st.pyplot(fig)

    st.subheader("Filas y columnas")
    st.write(df.shape)

    actual_prices = df.tail(1)
    st.subheader("Precios actuales")
    st.write(actual_prices)

    days = list()
    adj_close_prices = list()

    df_days = df.loc[:, 'Date']
    df_adj_close = df.loc[:, 'Adj Close']

    for day in df_days:
        days.append([int(day.split('-')[2])])

    for adj_close_price in df_adj_close:
        adj_close_prices.append(float(adj_close_price))

    st.subheader("Días separados encontrados del mes")
    st.write(days)

    st.subheader("Precio separado por días")
    st.write(adj_close_prices)

    st.subheader("Creación de modelos")
    
    # Se crea y entrena un modelo SVC con un kernel lineal
    svc_model = SVC(kernel='linear', C=1000.0)
    svc_model.fit(days, np.array(adj_close_prices) > np.mean(adj_close_prices))

    st.write("Predicción de tendencia según el modelo SVC:")
    st.write("Modelo SVC usando kernel lineal:", svc_model.predict(days))

    st.subheader("Comparación de modelos")
    fig1 = plt.figure(figsize=(16, 8))
    plt.scatter(days, adj_close_prices, color='red', label='data')
    plt.scatter(days, svc_model.predict(days), color='blue', label='Modelo SVC (Linear)')
    plt.title('Comparación de modelos')
    plt.legend()
    st.pyplot(fig1)

    st.write('Predicción de tendencia para el día dado:')
    st.write('Día = [[31]]')
    day = [[31]]
    st.subheader("SVC Predicción:")
    st.subheader(svc_model.predict(day))

if __name__ == "__main__":
    app()
