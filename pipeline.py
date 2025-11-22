# Pipeline ETL
import pandas as pd
import matplotlib.pyplot as plt

# ================EXTRACT===============================
# Extraindo os dados da planilha de gamesa

df = pd.read_csv("games.csv", sep=";")

# Dados brutos antes da transformação
print(df.head)

# =============TRANSFORM================================

# Eliminando a possibilidade de registros nulos e padronizando os títulos com iniciais maiúsculas
df = df.dropna()

df["titulo"] = df["titulo"].str.title()

df["preco"] = df["preco"].astype(float)
df["vendas"] = df["vendas"].astype(float)
df["nota"] = df["nota"].astype(float)

print(df.head)
# Metricas e agregações

df["receita_estim"] = df["preco"] * df["vendas"]

# Filtragem em jogos  com receita estimada acima de 1 bilhão

df_filtered = df[df["receita_estim"] > 1_000_000_000]

print(df_filtered.head)

# ====================LOAD=============================

# Criação do arquivo novo com os jogos mais vendidos
df_filtered.to_csv("games_most_sold.csv", sep=";", index=False)
print("Arquivo gerado com suceddo!")

# ==Gráficos

plt.figure(figsize=(10, 6))
