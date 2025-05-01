import os
import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.header("📡 Tecnologías de Conexión")
    st.write("Análisis de las tecnologías de conexión por localidad.")

    # Ruta absoluta
    data_path = os.path.join(os.path.dirname(__file__), "../data/Accesos_tecnologia_localidad_limpio.csv")
    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"Error: No se encontró el archivo {data_path}.")
        return
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return

    # Gráfico interactivo
    fig = px.bar(
        data,
        x="Localidad",
        y="Accesos",
        color="Tecnologia",  # Cambiado de "Tecnología" a "Tecnologia"
        title="Accesos por Tecnología y Localidad",
        labels={"Accesos": "Número de Accesos", "Localidad": "Localidad", "Tecnologia": "Tecnología"},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.subheader("Insights")
    st.markdown("""
    - **Tecnologías más utilizadas**: Identifica las tecnologías con mayor número de accesos.
    - **Localidades líderes**: Observa las localidades con mayor adopción tecnológica.
    """)