import pandas as pd

# 1. Cargar el archivo CSV con codificación UTF-8
df = pd.read_csv("dataset_tito.csv", encoding="utf-8")

# 2. Mostrar las primeras filas
print("--- PRIMERAS FILAS ---")
print(df.head())

# 3. Mostrar la cantidad total de filas
print("\n--- INFORMACIÓN GENERAL ---")
print("Cantidad total de preguntas:", len(df))

# 4. Mostrar los nombres de las columnas
print("Columnas en el dataset:", list(df.columns))

# 5. Mostrar las categorías únicas
print("\n--- CATEGORÍAS UNICAS ---")
print(df["categoria"].unique())

# 6. Contar la cantidad de preguntas por categoría
print("\n--- DISTRIBUCIÓN DE PREGUNTAS POR CATEGORÍA ---")
print(df["categoria"].value_counts())
