import pandas as pd

df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")
resumen = df["categoria"].value_counts().reset_index()
resumen.columns = ["categoria", "cantidad"]

print(resumen)
resumen.to_csv("resumen_corpus.csv", index=False, encoding="utf-8")