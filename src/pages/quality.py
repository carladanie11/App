import os
import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.header("📈 Calidad y Velocidad del Servicio")
    st.write("Análisis de las velocidades promedio de internet por provincia.")

    # Ruta absoluta
    data_path = os.path.join(os.path.dirname(__file__), "../data/Velocidad_por_provincia_limpio.csv")
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
        y="Mbps (Media de bajada)",
        color="Provincia",
        title="Velocidad promedio por provincia (Mbps)",
        labels={"Mbps (Media de bajada)": "Velocidad promedio (Mbps)"},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.subheader("Insights")
    st.markdown("""
    - **Provincias con mayor velocidad**: Capital Federal, Buenos Aires.
    - **Provincias con menor velocidad**: Chubut, Formosa.
    """)