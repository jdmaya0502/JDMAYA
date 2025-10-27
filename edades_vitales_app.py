import streamlit as st

st.title("🧬 Etapas vitales y costo de admisión")
st.markdown("___")  # línea separadora

# 🔹 Entrada de edad con control interactivo
edad = st.number_input("Ingresa tu edad:", min_value=0, step=1)

# 🔹 Determinar etapa vital
if edad < 2:
    etapa_vital = "BEBÉ"
elif edad < 4:
    etapa_vital = "NIÑO PEQUEÑO"
elif edad < 13:
    etapa_vital = "NIÑO"
elif edad < 21:
    etapa_vital = "ADOLESCENTE"
elif edad < 65:
    etapa_vital = "ADULTO"
else:
    etapa_vital = "ADULTO MAYOR"

# 🔹 Mostrar resultado
st.subheader("Etapa Vital:")
st.success(etapa_vital)

# 🔹 Calcular precio de admisión
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25.5
elif edad < 65:
    precio = 40
else:
    precio = 20

st.subheader("Costo de admisión:")
st.info(f"Costo de admisión para la edad de {edad:.0f} años: **${precio:.2f} pesos**")

st.markdown("___")
st.caption("Aplicación desarrollada con ❤️ en Streamlit")
