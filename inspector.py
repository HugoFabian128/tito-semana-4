import pandas as pd

df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")
cat_buscar = input("Escribe una categoría: ").strip().lower()

resultado = df[df["categoria"] == cat_buscar]

if len(resultado) == 0:
    print("No se encontró esa categoría.")
else:
    print(f"\nPreguntas en '{cat_buscar}':")
    for texto in resultado["texto"]:
        print("-", texto)