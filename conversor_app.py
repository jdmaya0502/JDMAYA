import streamlit as st

st.title("🌡️ Conversor de Temperatura")

st.write("Convierte entre Fahrenheit y Celsius de manera sencilla.")

# Entrada de temperatura
grados = st.number_input("Ingrese la temperatura:", value=0.0)

# Selección de escala
escala = st.radio(
    "Seleccione la escala de entrada:",
    ("Fahrenheit (F)", "Celsius (C)")
)

# Botón para convertir
if st.button("Convertir"):
    if escala == "Fahrenheit (F)":
        celsius = (grados - 32) / 1.8
        st.success(f"{grados} °F = {celsius:.2f} °C")

    elif escala == "Celsius (C)":
        fahrenheit = grados * 1.8 + 32
        st.success(f"{grados} °C = {fahrenheit:.2f} °F")