
# 📊 Análisis de Precios y Competencia

Esta es una aplicación web desarrollada con **Streamlit** que permite comparar los precios de productos de un negocio con los de su competencia y obtener alertas automáticas si los precios están muy caros o baratos.

---

## 🚀 ¿Qué hace esta app?

1. El usuario sube dos archivos `.csv`:
   - Uno con los precios del negocio
   - Otro con los precios de la competencia

2. La app compara ambos precios y calcula:
   - Diferencia absoluta
   - Diferencia porcentual
   - Alerta visual: ⚠️ Muy caro, 💸 Muy barato, ✅ Competitivo

3. Finalmente, permite **descargar un informe en Excel** con todos los resultados.

---

## 🧾 Formato de los archivos `.csv`

### 🟩 negocio.csv
```csv
Producto;Precio_Negocio
Hamburguesa;4500
Pizza;7000
Soda;1500
```

### 🟥 competencia.csv
```csv
Producto;Precio_Competencia
Hamburguesa;4000
Pizza;7300
Soda;1700
```

> **Nota:** Los campos deben estar separados por `;` (punto y coma), no por comas.

---

## 🌐 Prueba la app en línea

👉 [Haz clic aquí para usar la app](https://franco029-analisis-precios.streamlit.app/)

---

## 🛠️ Tecnologías usadas

- Python 🐍
- Streamlit ⚡
- Pandas 📊
- Openpyxl 📁

---

## 💡 Autor

Desarrollado por [Franco029](https://github.com/Franco029)
