import streamlit as st
from streamlit_lottie import st_lottie
import requests

# 👉 Función para cargar animación desde una URL
def load_lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# 🎯 Robot animado desde LottieFiles
robot_url = "https://assets6.lottiefiles.com/packages/lf20_zrqthn6o.json"
robot = load_lottieurl(robot_url)

# 🌐 Configuración de la página
st.set_page_config(
    page_title="Hostname",
    page_icon="🤖",
    layout="centered"
)

# 🎨 Estilos CSS con cajas azul claro y texto azul oscuro
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    .titulo {
        text-align: center;
        color: #2A6FDB;
        font-weight: 700;
        font-size: 36px;
        margin-bottom: 0;
    }

    .subtitulo {
        text-align: center;
        color: #6C757D;
        margin-top: -5px;
        font-size: 20px;
    }

    /* Estilo para el selectbox */
    div[data-baseweb="select"] > div {
        background-color: #e7f1ff !important;  /* azul claro */
        border-radius: 12px !important;
        border: 1px solid #b6d4fe !important;
        padding: 12px !important;
        font-size: 16px !important;
        color: #0c3c78 !important;
    }

    div[data-baseweb="select"] div[role="button"] span {
        color: #0c3c78 !important;
    }

    div[data-baseweb="select"] div[role="option"] {
        color: #0c3c78 !important;
    }

    /* Estilo para el input de texto */
    .stTextInput > div > input {
        background-color: #e7f1ff !important;  /* azul claro */
        border-radius: 12px !important;
        border: 1px solid #b6d4fe !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        color: #0c3c78 !important;
    }

    /* Botón */
    .stButton > button {
        margin-top: 12px;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 10px;
        background-color: #2A6FDB;
        color: white;
        font-weight: bold;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1e55a2;
    }

    /* Robot animado flotante */
    .robot-float {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 120px;
        z-index: 1000;
        pointer-events: none;
    }

    .robot-msg {
        position: fixed;
        bottom: 160px;
        right: 150px;
        background: #2A6FDB;
        color: white;
        padding: 10px 14px;
        border-radius: 10px;
        font-size: 16px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        z-index: 1001;
    }

    .robot-msg::after {
        content: "";
        position: absolute;
        bottom: -10px;
        right: 20px;
        border-width: 10px 10px 0;
        border-style: solid;
        border-color: #2A6FDB transparent transparent transparent;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 Título y subtítulo
st.markdown("<h1 class='titulo'>Contador Carácteres Hostname</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>CAASA</p>", unsafe_allow_html=True)

# 🔽 Selector y campo en una sola línea
col1, col2 = st.columns([1, 2])

with col1:
    opcion = st.selectbox("Seleccione tipo de Equipo:", ["", "PEPIPC", "PEPILA"])

with col2:
    if "texto_input" not in st.session_state:
        st.session_state.texto_input = ""
    if opcion and opcion != st.session_state.texto_input:
        st.session_state.texto_input = opcion
    texto = st.text_input("Ingresa el Hostname:", max_chars=15, key="texto_input")

# 🚀 Análisis de texto
if st.button("Ejecutar"):
    if not texto:
        st.warning("⚠️ Por favor ingresa algún texto.")
    else:
        total = len(texto)
        faltan = 15 - total
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"Total de caracteres: {total}")
        with col2:
            if faltan > 0:
                st.info(f"Faltan {faltan} para completar 15.")
            else:
                st.success("✅ ¡Exactamente 15 caracteres!")

# 🤖 Animación de robot flotante
with st.container():
    st.markdown('<div class="robot-float"></div>', unsafe_allow_html=True)
    st_lottie(robot, height=350, key="robot-float", speed=1, loop=True)
