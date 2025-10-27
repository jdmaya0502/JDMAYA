import streamlit as st

# Título principal
st.title("🧾 DATOS PERSONALES")

# Sección: datos básicos
st.header("👤 Información básica")

nombre = st.text_input("Nombre completo:", "Juan Diego Maya Hernandez")
edad = st.number_input("Edad:", min_value=0, max_value=120, value=43)

# Sección: vehículo
st.header("🚗 Información del vehículo")

carros = ["Aveo", "Spark", "Bicicleta"]
modelos = ["2010", "2015", "2020"]
versiones = ["Premier", "Activ", "LT"]

carro = st.selectbox("¿Qué vehículo conduces?", carros)
modelo = st.selectbox("¿Qué modelo es?", modelos)
version = st.selectbox("¿Cuál versión es?", versiones)

# Botón para mostrar resultados
if st.button("Mostrar información"):
    st.success("✅ Registro completado correctamente")
    
    st.write("### 🧾 Resumen de tus datos:")
    st.write(f"**Nombre:** {nombre.title()}")
    st.write(f"**Edad:** {edad} años")
    st.write(f"**Vehículo:** {carro}")
    st.write(f"**Modelo:** {modelo}")
    st.write(f"**Versión:** {version}")

    # Separador decorativo
    st.markdown("---")
    st.info("🚀 Gracias por usar la app de datos personales.")

