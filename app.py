import os
import streamlit as st
import pandas as pd
from openai import OpenAI
client = OpenAI()

OpenAI.api_key = st.secrets['OPENAI_API_KEY']

st.title("Asistente científico")

# Cargar el archivo CSV
csv_file = "data.csv"  # Asegúrate de que el archivo CSV esté en la raíz del proyecto

# Leer el archivo CSV
try:
  data = pd.read_csv(csv_file)
  st.dataframe(data)


    # Cuadro de texto para consultas sobre el CSV en la página principal
  consulta = st.text_input("Consulta:", "")

  if consulta:
    # Realizar la consulta a OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=1000,
        messages=[
            {"role": "system", "content": f"Eres un experto científico centrado en el análisis biológico de muestras con amplia experiencia en interpretación y análisis estadístico. Tu labor es encontrar patrones, tendencias y correlaciones entre datos de la temperatura y humedad relativa de una zona del desierto de Atacama. Tu función es ayudar a examinar datos de manera objetiva y proporcionar información valiosa. Según el siguiente conjunto de datos: {data}, responde a la consulta: {consulta}"}
        ]
    )
    
    # Mostrar la respuesta
    st.write("Respuesta de IA:")
    st.write(completion.choices[0].message.content)



except Exception as e:
  st.error(f"Error al cargar el archivo CSV: {e}")
  

