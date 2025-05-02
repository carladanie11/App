# Carlapp: Análisis del Sector de Telecomunicaciones en Argentina

![Carlapp Banner](https://via.placeholder.com/1200x300/1a254c/ffffff?text=Carlapp)

## 📋 Descripción

Carlapp es una aplicación interactiva desarrollada con Streamlit que permite visualizar y analizar datos del sector de telecomunicaciones en Argentina. Estos datos fueron obtenidos de [Dataset](https://datos.gob.ar/dataset?organization=enacom&tags=internet). La aplicación presenta información sobre penetración de servicios, calidad de conexión y tecnologías utilizadas en diferentes regiones del país de manera visual y atractiva.

## ✨ Características

- **Dashboard interactivo** con KPIs del sector telecomunicaciones
- **Visualizaciones dinámicas** con Plotly y componentes personalizados
- **Filtros avanzados** para analizar datos por provincia, tecnología y período
- **Interfaz responsiva** adaptada a diferentes dispositivos
- **Análisis detallado** con insights y recomendaciones
- **Experiencia de usuario mejorada** con animaciones y componentes interactivos

## 📊 Secciones

### 🏠 Inicio
Presenta un resumen general del sector con KPIs clave, mapa de cobertura e indicadores de desempeño.

### 📊 Penetración del Servicio
Análisis detallado de accesos por cada 100 hogares en diferentes provincias, con filtros por año y nivel de penetración.

### 📈 Calidad y Velocidad
Análisis de velocidades promedio de internet por provincia, con comparativas y evolución temporal.

### 🔌 Tecnologías de Conexión
Análisis de la distribución de tecnologías por localidad, con mapas de calor y visualizaciones interactivas.

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/telecovision.git
cd telecovision

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
```

## 🚀Streamoku
Para desplegar la aplicación en [Streamoku](https://streamoku.com), sigue estos pasos:

1. **Inicia sesión o regístrate** en [Streamoku](https://streamoku.com).

2. **Crea un nuevo proyecto**:
    - Haz clic en el botón "New Project".
    - Asigna un nombre al proyecto y selecciona la opción para desplegar desde un repositorio de GitHub.

3. **Conecta el repositorio**:
    - Autoriza a Streamoku para acceder a tu cuenta de GitHub.
    - Selecciona el repositorio desde tu lista de repositorios.

4. **Despliega la aplicación**:
    - Haz clic en "Deploy" para iniciar el proceso de despliegue.
    - Una vez completado, obtendrás un enlace público para acceder a tu aplicación.


## 📦 Requisitos

Consulta el archivo `requirements.txt` para ver las dependencias necesarias:

- streamlit
- pandas
- plotly
- streamlit-extras
- streamlit-lottie
- requests

## 📁 Estructura del Proyecto

```
telecovision/
├── app.py                   # Aplicación principal
├── requirements.txt         # Dependencias
├── src/                     # Código fuente
│   ├── data/                # Archivos de datos
│   │   ├── Penetracion_hogares_limpio.csv
│   │   ├── Velocidad_por_provincia_limpio.csv
│   │   └── Accesos_tecnologia_localidad_limpio.csv
├── LICENSE                  # Licencia
└── README.md                # Documentación
```


## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- [Streamlit](https://streamlit.io/) por la plataforma de desarrollo
- [Plotly](https://plotly.com/) por las visualizaciones interactivas
- [Streamlit-Extras](https://github.com/arnaudmiribel/streamlit-extras) por los componentes adicionales