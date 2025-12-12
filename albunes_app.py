import streamlit as st
import json
import os
import pandas as pd

# Archivo donde se guardarán los álbumes
ARCHIVO_JSON = "albunes.json"

# ----------------------------------------------------------
# Funciones
# ----------------------------------------------------------
def hacer_albun(artista, titulo, traks=None):
    albun = {"artista": artista, "titulo": titulo}
    if traks:
        albun["traks"] = traks
    return albun


def guardar_json(data):
    with open(ARCHIVO_JSON, "w") as f:
        json.dump(data, f, indent=4)


def cargar_json():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r") as f:
            return json.load(f)
    return []


# ----------------------------------------------------------
# Inicializar sesión
# ----------------------------------------------------------
if "albunes" not in st.session_state:
    st.session_state.albunes = cargar_json()  # cargar si existe archivo


# ----------------------------------------------------------
# Interfaz (sidebar)
# ----------------------------------------------------------
st.sidebar.title("⚙️ Opciones")

if st.sidebar.button("💾 Guardar álbumes en archivo JSON"):
    guardar_json(st.session_state.albunes)
    st.sidebar.success("Álbumes guardados correctamente.")

if st.sidebar.button("🗑️ Borrar todos los álbumes"):
    st.session_state.albunes = []
    guardar_json([])
    st.sidebar.warning("Todos los álbumes fueron eliminados.")


st.sidebar.write("---")
st.sidebar.write("Desarrollado por **Juan Diego** 🎵")


# ----------------------------------------------------------
# Título principal
# ----------------------------------------------------------
st.title("🎧 Registro Profesional de Álbumes Musicales")


# ----------------------------------------------------------
# Formulario
# ----------------------------------------------------------
st.header("➕ Agregar nuevo álbum")

with st.form("formulario_albun"):
    artista = st.text_input("Artista").upper()
    titulo = st.text_input("Título").upper()
    traks = st.text_input("Número de tracks (opcional)")

    enviado = st.form_submit_button("Agregar álbum")

    if enviado:
        if artista.strip() == "" or titulo.strip() == "":
            st.error("El artista y el título son obligatorios.")
        else:
            if traks.strip() == "":
                albun = hacer_albun(artista, titulo)
            else:
                albun = hacer_albun(artista, titulo, traks)

            st.session_state.albunes.append(albun)
            st.success("Álbum agregado correctamente ✔️")


# ----------------------------------------------------------
# Mostrar álbumes en lista bonita
# ----------------------------------------------------------
st.header("📀 Álbumes registrados")

if len(st.session_state.albunes) == 0:
    st.info("Aún no has registrado ningún álbum.")
else:
    for i, albun in enumerate(st.session_state.albunes):
        with st.expander(f"🎵 {albun['artista']} - {albun['titulo']}"):
            st.write(f"**Artista:** {albun['artista']}")
            st.write(f"**Título:** {albun['titulo']}")
            if "traks" in albun:
                st.write(f"**Tracks:** {albun['traks']}")

            eliminar = st.button(f"Eliminar álbum #{i+1}", key=f"del_{i}")
            if eliminar:
                st.session_state.albunes.pop(i)
                guardar_json(st.session_state.albunes)
                st.warning("Álbum eliminado.")
                st.rerun()


# ----------------------------------------------------------
# Tabla con los álbumes
# ----------------------------------------------------------
st.header("📊 Tabla de álbumes")

if len(st.session_state.albunes) > 0:
    df = pd.DataFrame(st.session_state.albunes)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No hay álbumes para mostrar.")