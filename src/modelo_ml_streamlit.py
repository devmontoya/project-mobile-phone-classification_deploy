# Se utiliza como template el código dado en clase

import streamlit as st #Para hacer una web de datos
from PIL import Image #Para el manejo de imágenes
import pandas as pd #Para generar los Dataframes de mis CSV
import time #Para la parte de sincronía y para medir el tiemp de procesamiento

import joblib #Usado para cargar Pipeline
import numpy as np #Para operaciones matemáticas
import matplotlib.pyplot as plt #Para plotear algunas gráficas (Histogramas)

#------------------------------------------------------------------------------------------------
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

import Preprocessors.preprocessors as pp
#------------------------------------------------------------------------------------------------

def preprocesado_prediccion(pipeline_de_test, datos_de_test):
    #Dropeamos
    #datos_de_test.drop('Id', axis=1, inplace=True)

    predicciones = pipeline_de_test.predict(datos_de_test)

    return predicciones, datos_de_test

#Diseno de la Interface
st.title("Mobile price range predictor - Daniel Montoya - DATAPATH")

image = Image.open('src/images/mobile_store.jpeg') #COMPLETAR CON UNA IMAGEN
st.image(image, use_container_width=True)

st.sidebar.write("Suba el archivo CSV correspondiente para realizar la predicción")

#------------------------------------------------------------------------------------------
# Cargar el archivo CSV desde la barra lateral
uploaded_file = st.sidebar.file_uploader(" ", type=['csv'])

if uploaded_file is not None:
    #Leer el archivo CSV y lo pasamos a Dataframe
    df_de_los_datos_subidos = pd.read_csv(uploaded_file)

    #Mostrar el contenido del archivo CSV
    st.write('Contenido del archivo CSV:')
    st.dataframe(df_de_los_datos_subidos)
#-------------------------------------------------------------------------------------------
#Se cargar el Pipeline
pipeline_de_produccion = joblib.load('./src/Pipelines/prange_ml_pipeline.joblib')

if st.sidebar.button("click aqui para enviar el CSV al Pipeline"):
    if uploaded_file is None:
        st.sidebar.write("No se cargó correctamente el archivo, subalo de nuevo")
    else:
        with st.spinner('Pipeline y Modelo procesando...'):

            prediccion, datos_procesados = preprocesado_prediccion(pipeline_de_produccion, df_de_los_datos_subidos)
            time.sleep(5)
            st.success('Listo!')

            # Mostramos los resultados de la predicción
            st.write('Resultados de la predicción:')
            st.write(prediccion)

            #Graficar los precios de venta predichos
            fig, ax = plt.subplots()
            pd.Series(prediccion).hist(bins=50, ax=ax)
            ax.set_title('Histograma de los rangos de precios predichos')
            ax.set_xlabel('Rango de precio')
            ax.set_ylabel('Frecuencia')

            #Mostramos la gráfica en Streamlit
            st.pyplot(fig)

            #Proceso para descargar todo el archivo con las predicciones
            #----------------------------------------------------------------------------
            #Concatenamos predicciones con el archivo original subido
            df_resultado = datos_procesados.copy()
            df_resultado['Predicción'] = prediccion

            #Mostrar el Dataframe contatenado
            st.write('Datos originales con predicciones:')
            st.dataframe(df_resultado)

            csv = df_resultado.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download CSV file with predictions",
                data=csv,
                file_name='mobile_phone_range_predictions.csv',
                mime='text/csv',
            )
            #-------------------------------------------------------------------

#Comando para lanzar la aplicación de forma LOCAL:
#streamlit run modelo_ml_streamlit.py
