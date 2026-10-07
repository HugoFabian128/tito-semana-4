import pandas as pd

# 1. Cargar el dataset original
print("Cargando dataset_tito.csv...")
df = pd.read_csv("dataset_tito.csv", encoding="utf-8")

print(f"Filas iniciales: {len(df)}")
print(f"Duplicados iniciales: {df.duplicated().sum()}")
print(f"Valores faltantes por columna:\n{df.isnull().sum()}\n")

# --- PASO 4: PROCESO DE LIMPIEZA ---

# A. Eliminar filas con valores nulos/vacíos
df = df.dropna(subset=["texto", "categoria"])

# B. Limpiar espacios en blanco al inicio/final y pasar categorías a minúsculas
df["texto"] = df["texto"].astype(str).str.strip()
df["categoria"] = df["categoria"].astype(str).str.strip().str.lower()

# C. Filtrar cadenas de texto vacías
df = df[(df["texto"] != "") & (df["categoria"] != "")]

# D. Eliminar filas duplicadas
df = df.drop_duplicates()

# --- PASO 9: GUARDAR EN DATASET_TITO_V1.CSV ---

# Guardar la versión v1 limpia
df.to_csv("dataset_tito_v1.csv", index=False, encoding="utf-8")

print("==========================================")
print("¡Limpieza completada y dataset v1 guardado!")
print("==========================================")
print(f"Filas finales en dataset_tito_v1.csv: {len(df)}")
print("\nDistribución final por categoría:")
print(df["categoria"].value_counts())