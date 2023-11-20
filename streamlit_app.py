import streamlit as st
from multiapp import MultiApp

# import los modelos aqui
from apps import home, svr, svc, forecasting

app = MultiApp()

st.markdown(
    """
# Proyecto Integrador - G3
"""
)
# Add all your application here
app.add_app("Inicio", home.app)
app.add_app("Modelo SVR", svr.app)
app.add_app("Modelo SVC", svc.app)
app.add_app("Forecasting", forecasting.app)

# The main app
app.run()
