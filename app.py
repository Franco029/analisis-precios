
import streamlit as st
import pandas as pd
import io

streamlit
pandas
openpyxl

st.set_page_config(page_title="Análisis de Precios", layout="centered")
st.title("🔍 Análisis de Precios y Competencia")

st.write("Sube dos archivos CSV: uno con los precios de tu negocio y otro con los de la competencia.")

# Subir archivos
archivo_negocio = st.file_uploader("Archivo de tu negocio (.csv)", type=["csv"])
archivo_competencia = st.file_uploader("Archivo de la competencia (.csv)", type=["csv"])

if archivo_negocio and archivo_competencia:
    df_negocio = pd.read_csv(archivo_negocio, sep=";")
    df_competencia = pd.read_csv(archivo_competencia, sep=";")

    # Renombrar columnas
    df_negocio.columns = ["Producto", "Precio_Negocio"]
    df_competencia.columns = ["Producto", "Precio_Competencia"]

    # Merge
    df = pd.merge(df_negocio, df_competencia, on="Producto")
    df["Diferencia"] = df["Precio_Negocio"] - df["Precio_Competencia"]
    df["Porcentaje_Diferencia"] = ((df["Diferencia"] / df["Precio_Competencia"]) * 100).round(2)

    def alerta(row):
        if row["Porcentaje_Diferencia"] > 20:
            return "⚠️ Muy caro"
        elif row["Porcentaje_Diferencia"] < -20:
            return "💸 Muy barato"
        else:
            return "✅ Competitivo"

    df["Alerta"] = df.apply(alerta, axis=1)

    st.success("✅ Análisis completo")
    st.dataframe(df)

    # Descargar Excel
    output = io.BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Descargar informe Excel", output.getvalue(), file_name="informe_analisis_precios.xlsx")
