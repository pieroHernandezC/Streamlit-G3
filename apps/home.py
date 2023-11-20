import streamlit as st

def app():

    st.subheader('INTEGRANTES:')   
    st.write('Benites Narrea, Elvis Saul')
    st.write('Hernandez Cordova, Piero Josue')
    st.write('Huallpartupa Gallegos, Wilfredo') 
    st.write('Ramos Villanueva, Sebastian Elias')
    st.write('Vega Centeno, Rodrigo Sebastian')        
    
    # Agregar la imagen desde el enlace
    imagen_link = "https://estudiaperu.pe/wp-content/uploads/2019/10/UNMSM-300x119.png"
    st.image(imagen_link, caption='UNMSM', use_column_width=True)

    st.write(st.__version__)

    st.write(st.__version__)