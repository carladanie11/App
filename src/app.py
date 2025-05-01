import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Análisis del Sector de Telecomunicaciones",
    page_icon="📡",
    layout="wide"
)

# Título principal
st.title("📡 Análisis del Sector de Telecomunicaciones en Argentina")

# Sidebar para navegación
st.sidebar.title("Navegación")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    ("Inicio", "Penetración del Servicio", "Calidad y Velocidad", "Tecnologías de Conexión")
)

# Función para manejar errores al cargar datos
def cargar_datos(ruta):
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        st.error(f"Error: No se encontró el archivo {ruta}.")
        return None
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Cargar las páginas según la selección
if seccion == "Inicio":
    st.write("Bienvenido al análisis interactivo del sector de telecomunicaciones en Argentina.")
    st.write("Selecciona una sección en la barra lateral para explorar los datos.")
elif seccion == "Penetración del Servicio":
    import pages.penetration as penetration
    penetration.show()
elif seccion == "Calidad y Velocidad":
    import pages.quality as quality
    quality.show()
elif seccion == "Tecnologías de Conexión":
    import pages.technologies as technologies
    technologies.show()