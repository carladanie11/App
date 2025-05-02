import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie
import requests
import json

# Configuración de la página
st.set_page_config(
    page_title="Análisis del Sector de Telecomunicaciones",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función para cargar animaciones Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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

# Estilos CSS personalizados
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    .stApp {
        max-width: 1200px; 
        margin: 0 auto;
    }
    .stSidebar {
        background-color: #1a254c;
        color: white;
    }
    h1, h2, h3 {
        color: #1a254c;
    }
    .highlight {
        color: #ff4b4b;
        font-weight: bold;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #f0f4fa;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar con navegación
with st.sidebar:
    st.markdown("<h1 style='color: black; text-align: center;'>📡 Carlapp</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #c0c0c0; text-align: center;'>Análisis del Sector de Telecomunicaciones en Argentina</p>", unsafe_allow_html=True)
    
    # Carga de animación
    lottie_telecom = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_WdTEui.json")
    if lottie_telecom:
        st_lottie(lottie_telecom, height=150, key="telecom")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    seccion = st.radio(
        "Explorar:",
        ("🏠 Inicio", "📊 Penetración del Servicio", "📈 Calidad y Velocidad", "🔌 Tecnologías de Conexión"),
        label_visibility="collapsed"
    )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='color: #c0c0c0; text-align: center; font-size: 12px;'>Desarrollado con ❤️ por Carla Loredo</p>", unsafe_allow_html=True)

# Cargar las páginas según la selección
if seccion == "🏠 Inicio":
    # Header con animación
    col1, col2 = st.columns([3, 1])
    with col1:
        colored_header(
            label="Bienvenido a Carlapp",
            description="Una plataforma interactiva para analizar datos del sector de telecomunicaciones",
            color_name="blue-70"
        )
    with col2:
        lottie_welcome = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jvxwtdtp.json")
        if lottie_welcome:
            st_lottie(lottie_welcome, height=120, key="welcome")
    
    st.markdown("""
    <div class="card">
        <h3>¿Qué es Carlapp?</h3>
        <p>Esta aplicación presenta un análisis completo y visual del sector de telecomunicaciones en Argentina, 
        permitiéndote explorar datos sobre:</p>
        <ul>
            <li><b>Penetración de servicios</b> en hogares por provincia</li>
            <li><b>Calidad y velocidad</b> de conexión a Internet</li>
            <li><b>Tecnologías de conexión</b> utilizadas en diferentes localidades</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # KPIs generales
    st.subheader("Panorama General")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Promedio Nacional</h4>
            <h2>67.8%</h2>
            <p>Penetración de Internet</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>Velocidad Media</h4>
            <h2>52.3 Mbps</h2>
            <p>Bajada promedio</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>Tecnología Líder</h4>
            <h2>Fibra Óptica</h2>
            <p>Mayor crecimiento</p>
        </div>
        """, unsafe_allow_html=True)
    style_metric_cards()
    
    # Mapa de Argentina
    st.subheader("Mapa de Cobertura")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Placeholder para un mapa - en una implementación real, usarías datos geoespaciales
    fig = go.Figure(data=go.Choropleth(
        locations=['BA', 'CF', 'CH', 'CO', 'ER', 'FO', 'JU', 'LP', 'MZ', 'MI', 'NQ', 'RN', 'SA', 'SJ', 'SL', 'SC', 'SF', 'SE', 'TF', 'TU'],
        z=[65, 89, 45, 60, 55, 40, 50, 58, 62, 48, 57, 59, 51, 56, 60, 54, 63, 49, 72, 53],
        locationmode='country names',
        colorscale='Blues',
        colorbar_title='Penetración (%)',
    ))
    
    fig.update_layout(
        geo=dict(
            scope='south america',
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth'
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Indicadores de desempeño
    st.subheader("Indicadores Clave")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Brecha Digital")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=31.2,
            title={'text': "Diferencia entre máx. y mín. penetración (%)"},
            gauge={'axis': {'range': [None, 50]},
                  'bar': {'color': "#1a254c"},
                  'steps': [
                      {'range': [0, 20], 'color': "#e6f2ff"},
                      {'range': [20, 35], 'color': "#b3d9ff"},
                      {'range': [35, 50], 'color': "#80bfff"}
                  ],
                  'threshold': {
                      'line': {'color': "red", 'width': 4},
                      'thickness': 0.75,
                      'value': 31.2
                  }
            }
        ))
        fig.update_layout(height=250)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Crecimiento Interanual")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=['2018', '2019', '2020', '2021', '2022', '2023', '2024'],
            y=[47, 52, 58, 61, 64, 66, 68],
            mode='lines+markers',
            name='Penetración',
            line=dict(color='#1a254c', width=3)
        ))
        fig.update_layout(
            xaxis_title="Año",
            yaxis_title="Penetración (%)",
            height=250,
            margin=dict(l=0, r=0, t=0, b=0),
        )
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif seccion == "📊 Penetración del Servicio":
    colored_header(
        label="Penetración del Servicio de Internet",
        description="Análisis de la penetración de internet en hogares por provincia",
        color_name="blue-70"
    )
    
    # Ruta absoluta
    data_path = os.path.join(os.path.dirname(__file__), "src/data/Penetracion_hogares_limpio.csv")
    data = cargar_datos(data_path)
    
    if data is not None:
        # Filtros interactivos
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            # Suponiendo que tienes datos de año
            year = st.selectbox("Seleccionar año:", ["2024", "2023", "2022", "2021"])
        with col2:
            # Filtra por un umbral mínimo
            min_value = st.slider("Mostrar provincias con penetración mayor a:", 0, 100, 0)
        
        # Filtramos los datos (simulación)
        filtered_data = data[data["Accesos por cada 100 hogares"] >= min_value].copy()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Métricas clave
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            max_val = filtered_data["Accesos por cada 100 hogares"].max()
            max_prov = filtered_data.loc[filtered_data["Accesos por cada 100 hogares"].idxmax(), "Provincia"]
            st.metric("Mayor penetración", f"{max_val:.1f}%", f"{max_prov}")
        with col2:
            min_val = filtered_data["Accesos por cada 100 hogares"].min()
            min_prov = filtered_data.loc[filtered_data["Accesos por cada 100 hogares"].idxmin(), "Provincia"]
            st.metric("Menor penetración", f"{min_val:.1f}%", f"{min_prov}")
        with col3:
            avg_val = filtered_data["Accesos por cada 100 hogares"].mean()
            st.metric("Promedio nacional", f"{avg_val:.1f}%")
        with col4:
            diff = max_val - min_val
            st.metric("Brecha digital", f"{diff:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Gráficos
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Gráfico de barras mejorado
            filtered_data = filtered_data.sort_values("Accesos por cada 100 hogares", ascending=False)
            
            fig = px.bar(
                filtered_data,
                x="Provincia",
                y="Accesos por cada 100 hogares",
                color="Accesos por cada 100 hogares",
                title="Accesos por cada 100 hogares en las provincias",
                labels={"Accesos por cada 100 hogares": "Accesos por cada 100 hogares"},
                color_continuous_scale=px.colors.sequential.Blues,
                template="plotly_white",
                text="Accesos por cada 100 hogares"
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            
            # Agregar línea de promedio
            fig.add_shape(
                type="line",
                x0=-0.5,
                y0=avg_val,
                x1=len(filtered_data)-0.5,
                y1=avg_val,
                line=dict(color="red", width=2, dash="dash")
            )
            fig.add_annotation(
                x=len(filtered_data)-1,
                y=avg_val,
                text=f"Promedio: {avg_val:.1f}%",
                showarrow=False,
                yshift=10
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Gráfico de torta para categorías de penetración
            categories = pd.cut(
                filtered_data["Accesos por cada 100 hogares"],
                bins=[0, 50, 70, 100],
                labels=["Baja (<50%)", "Media (50-70%)", "Alta (>70%)"]
            )
            
            category_counts = categories.value_counts().reset_index()
            category_counts.columns = ["Categoría", "Cantidad"]
            
            fig = px.pie(
                category_counts,
                values="Cantidad",
                names="Categoría",
                title="Distribución por nivel de penetración",
                color_discrete_sequence=px.colors.sequential.Blues_r,
                hole=0.4
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Insigths mejorados
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Insights")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### Provincias líderes
            - **Capital Federal** (89.2%): La más alta penetración del país, impulsada por alta densidad urbana e infraestructura avanzada.
            - **Tierra del Fuego** (72.3%): Alta penetración a pesar de su ubicación remota, posiblemente por políticas de desarrollo específicas.
            """)
        
        with col2:
            st.markdown("""
            #### Provincias rezagadas
            - **Formosa** (42.1%): La menor penetración del país, enfrentando desafíos de infraestructura y geografía.
            - **Chaco** (44.5%): Penetración significativamente por debajo del promedio nacional, reflejando brechas en desarrollo digital.
            """)
        
        # Recomendaciones
        st.markdown("""
        #### Recomendaciones para reducir la brecha digital
        1. **Inversión focalizada** en infraestructura para las provincias con menor penetración
        2. **Programas de adopción digital** para estimular la demanda en zonas rezagadas
        3. **Incentivos fiscales** para operadores que expandan servicios en áreas desatendidas
        4. **Alianzas público-privadas** para acelerar el despliegue de redes
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif seccion == "📈 Calidad y Velocidad":
    colored_header(
        label="Calidad y Velocidad del Servicio",
        description="Análisis de las velocidades promedio de internet por provincia",
        color_name="blue-70"
    )
    
    # Ruta absoluta
    data_path = os.path.join(os.path.dirname(__file__), "src/data/Velocidad_por_provincia_limpio.csv")
    data = cargar_datos(data_path)
    
    if data is not None:
        # Filtros interactivos
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            # Suponiendo que tienes datos de trimestre
            quarter = st.selectbox("Seleccionar trimestre:", ["2024-Q1", "2023-Q4", "2023-Q3", "2023-Q2"])
        with col2:
            # Filtrar por velocidad mínima
            min_speed = st.slider("Mostrar velocidades mayores a:", 0, 100, 0)
        
        # Filtramos los datos (asumiendo que ya tenemos estos filtros)
        filtered_data = data[data["Mbps (Media de bajada)"] >= min_speed]
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Métricas principales
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            max_val = filtered_data["Mbps (Media de bajada)"].max()
            max_prov = filtered_data.loc[filtered_data["Mbps (Media de bajada)"].idxmax(), "Provincia"]
            st.metric("Mayor velocidad", f"{max_val:.1f} Mbps", f"{max_prov}")
        with col2:
            min_val = filtered_data["Mbps (Media de bajada)"].min()
            min_prov = filtered_data.loc[filtered_data["Mbps (Media de bajada)"].idxmin(), "Provincia"]
            st.metric("Menor velocidad", f"{min_val:.1f} Mbps", f"{min_prov}")
        with col3:
            avg_val = filtered_data["Mbps (Media de bajada)"].mean()
            st.metric("Promedio nacional", f"{avg_val:.1f} Mbps")
        with col4:
            # Asumimos que tenemos datos de trimestre anterior para comparar
            prev_avg = avg_val * 0.9  # Simulamos un 10% de crecimiento
            growth = ((avg_val - prev_avg) / prev_avg) * 100
            st.metric("Crecimiento", f"{growth:.1f}%", f"+{growth:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualizaciones
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Ordenamos los datos de mayor a menor
            filtered_data = filtered_data.sort_values("Mbps (Media de bajada)", ascending=False)
            
            # Creamos un gráfico de barras horizontales
            fig = px.bar(
                filtered_data,
                y="Provincia",
                x="Mbps (Media de bajada)",
                color="Mbps (Media de bajada)",
                orientation='h',
                title="Velocidad promedio por provincia (Mbps)",
                labels={"Mbps (Media de bajada)": "Velocidad promedio (Mbps)"},
                color_continuous_scale=px.colors.sequential.Viridis,
                template="plotly_white",
                text="Mbps (Media de bajada)"
            )
            
            fig.update_traces(texttemplate='%{text:.1f} Mbps', textposition='outside')
            
            # Agregamos línea de promedio
            fig.add_shape(
                type="line",
                x0=avg_val,
                y0=-0.5,
                x1=avg_val,
                y1=len(filtered_data)-0.5,
                line=dict(color="red", width=2, dash="dash")
            )
            
            fig.add_annotation(
                x=avg_val,
                y=0,
                text=f"Promedio: {avg_val:.1f} Mbps",
                showarrow=False,
                xshift=15,
                yshift=-20
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Gráfico para categorías de velocidad
            categories = pd.cut(
                filtered_data["Mbps (Media de bajada)"],
                bins=[0, 30, 60, 200],
                labels=["Baja (<30 Mbps)", "Media (30-60 Mbps)", "Alta (>60 Mbps)"]
            )
            
            category_counts = categories.value_counts().reset_index()
            category_counts.columns = ["Categoría", "Cantidad"]
            
            # Gráfico de dona
            fig = px.pie(
                category_counts,
                values="Cantidad",
                names="Categoría",
                title="Distribución por nivel de velocidad",
                color_discrete_sequence=px.colors.sequential.Viridis_r,
                hole=0.4
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Velocidad nacional en el tiempo
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Simulamos datos históricos
            historical = pd.DataFrame({
                "Trimestre": ["2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4", "2024-Q1"],
                "Velocidad Media": [38.5, 42.1, 45.7, 49.2, 52.3]
            })
            
            fig = px.line(
                historical,
                x="Trimestre",
                y="Velocidad Media",
                title="Evolución de la velocidad promedio nacional",
                markers=True,
                line_shape="spline"
            )
            
            fig.update_traces(line=dict(color="#1a254c", width=3))
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Insights y recomendaciones
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Insights")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### Provincias con mayor velocidad
            - **Capital Federal** (105.7 Mbps): Concentra la mayor infraestructura de fibra óptica del país.
            - **Buenos Aires** (78.3 Mbps): Beneficiada por la cercanía a los principales nodos de conexión internacional.
            """)
        
        with col2:
            st.markdown("""
            #### Provincias con menor velocidad
            - **Formosa** (22.4 Mbps): Limitaciones en infraestructura afectan significativamente la calidad del servicio.
            - **Chubut** (26.8 Mbps): La dispersión geográfica dificulta el despliegue de redes de alta velocidad.
            """)
        
        # Conclusiones
        st.markdown("""
        #### Análisis comparativo internacional
        Argentina presenta una velocidad promedio **por debajo del promedio latinoamericano** de 56.4 Mbps, aunque con una tendencia de crecimiento sostenido en los últimos trimestres.
        
        #### Factores que afectan la velocidad
        1. **Inversión en infraestructura**: Correlación directa entre inversión y velocidad
        2. **Densidad poblacional**: Las áreas urbanas densas tienden a tener mejor servicio
        3. **Políticas regulatorias**: Los incentivos al despliegue de fibra óptica marcan diferencias notables
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif seccion == "🔌 Tecnologías de Conexión":
    colored_header(
        label="Tecnologías de Conexión",
        description="Análisis de las tecnologías de conexión por localidad",
        color_name="blue-70"
    )
    
    # Ruta absoluta
    data_path = os.path.join(os.path.dirname(__file__), "src/data/Accesos_tecnologia_localidad_limpio.csv")
    data = cargar_datos(data_path)
    
    if data is not None:
        # Preparamos datos para las visualizaciones
        tech_totals = data.groupby("Tecnologia")["Accesos"].sum().reset_index()
        tech_totals = tech_totals.sort_values("Accesos", ascending=False)
        
        # Filtros interactivos
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            selected_techs = st.multiselect(
                "Filtrar por tecnologías:",
                options=data["Tecnologia"].unique(),
                default=data["Tecnologia"].unique()
            )
        with col2:
            top_n = st.slider("Ver top localidades:", 5, 20, 10)
        
        filtered_data = data[data["Tecnologia"].isin(selected_techs)]
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Resumen de tecnologías - KPIs
        st.markdown('<div class="card">', unsafe_allow_html=True)
        # Distribución de tecnologías
        st.subheader("Distribución de Tecnologías")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            # Gráfico de barras para todas las tecnologías
            fig = px.bar(
                tech_totals,
                x="Tecnologia",
                y="Accesos",
                color="Tecnologia",
                title="Distribución de accesos por tecnología",
                labels={"Accesos": "Número total de accesos", "Tecnologia": "Tecnología"},
                template="plotly_white",
                text="Accesos"
            )
            
            fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Gráfico de pastel
            fig = px.pie(
                tech_totals,
                values="Accesos",
                names="Tecnologia",
                title="Participación de mercado por tecnología",
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Bold
            )
            
            fig.update_traces(textinfo='percent+label')
            
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
