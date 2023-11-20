import streamlit as st
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def app():
    st.title("Modelo SVR para Forecasting")
    st.title("Predicción de precios de cierre ajustados utilizando SVR")

    start = st.date_input("Inicio (Start)", value=pd.to_datetime("2022-12-01"))
    end = st.date_input("Fin (End)", value=pd.to_datetime("today"))
    user_input = st.text_input("Introducir cotización bursátil", "AVGO")

    df = yf.download(user_input, start, end)
   # df.index = df.index.strftime('%Y-%m-%d')
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

    st.subheader("Creación de modelo SVR para forecasting")
    
    # Se crea y entrena un modelo SVR con un kernel rbf para forecasting
    rbf_svr_forecast = SVR(kernel='rbf', C=1000.0, gamma=0.15)
    rbf_svr_forecast.fit(days, adj_close_prices)

    st.write("Predicción de precios de cierre ajustados para días futuros:")
    future_days = [[day] for day in range(max(days)[0] + 1, max(days)[0] + 6)]  # Predicción para los próximos 5 días
    forecasted_prices = rbf_svr_forecast.predict(future_days)

    forecast_df = pd.DataFrame({
        'Fecha': [df['Date'].max() + pd.DateOffset(days=i) for i in range(1, 6)],
        'Predicción Precio Cierre': forecasted_prices
    })

    st.write(forecast_df)

    st.subheader("Visualización de la predicción")
    fig1 = plt.figure(figsize=(16, 8))
    plt.scatter(days, adj_close_prices, color='red', label='Datos históricos')
    plt.plot(future_days, forecasted_prices, color='green', label='Predicción')
    plt.title('Predicción de precios de cierre ajustados para días futuros')
    plt.xlabel('Días')
    plt.ylabel('Precio Cierre Ajustado')
    plt.legend()
    st.pyplot(fig1)

if __name__ == "__main__":
    app()
