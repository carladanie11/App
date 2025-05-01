import os
import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.header("📊 Penetración del Servicio")
    st.write("Análisis de la penetración de internet en hogares y población.")

    # Ruta absoluta
    data_path = os.path.join(os.path.dirname(__file__), "../data/Penetracion_hogares_limpio.csv")
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
        x="Provincia",
        y="Accesos por cada 100 hogares",
        color="Provincia",
        title="Accesos por cada 100 hogares en las provincias",
        labels={"Accesos por cada 100 hogares": "Accesos por cada 100 hogares"},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.subheader("Insights")
    st.markdown("""
    - **Provincias líderes**: Capital Federal, Tierra del Fuego.
    - **Provincias rezagadas**: Formosa, Chaco.
    """)