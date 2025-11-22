import pandas as pd
import matplotlib.pyplot as plt

# IDE UTILIZADA: Spyder


# ==================EXTRAÇÃO=================================
# Aqui extraimos os dados de uma planilha que contém informações de jogos que foram bem sucedidos em seus gêneros nos últimos anos
# As colunas dessa tabela são id, titulo, genero, preco, nota e vendas.
# A partir disso, foi utilizado a biblioteca pandas para a extração desses dados para o uso da etapa de transform


df = pd.read_csv("games.csv", sep=";")

# ==================TRANSFORMAÇÃO============================
# Aqui é passado uma serie de alterações para prover dados adicionais para a planilha, além de atualiza-la.

# Calcular receita estimada
df["receita_estimativa"] = df["preco"] * df["vendas"]

# Criar categoria de vendas para adicionar em cada game seu desempenho em vendas


def categoria_vendas(v):
    if v < 1_000_000:
        return "baixa"
    elif v < 10_000_000:
        return "media"
    else:
        return "alta"


df["categoria_vendas"] = df["vendas"].apply(categoria_vendas)

# Criar categoria de nota para cada jogo


def categoria_nota(n):
    if n < 6:
        return "ruim"
    elif n < 8:
        return "boa"
    else:
        return "excelente"


df["categoria_nota"] = df["nota"].apply(categoria_nota)

# Ordenar jogos por melhor nota
df_sorted_nota = df.sort_values(by="nota", ascending=False)

# Ordenar jogos por maior receita
df_sorted_receita = df.sort_values(by="receita_estimativa", ascending=False)

# Agrupar por gênero (métricas úteis)
metricas_genero = df.groupby(
    "genero")[["nota", "vendas", "receita_estimativa"]].mean()

# ==================LOAD============================
# Utilizando o matplotlib, criamos alguns gráficos com o resultado tirado de toda a transformação da planilha extraida

# Criando a planilha atualizada
df.to_csv("games_transformado.csv", sep=";", index=False)

# GRÁFICOS

# Gráfico 1 - Top receitas
top_receita = df_sorted_receita.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_receita["titulo"], top_receita["receita_estimativa"])
plt.xticks(rotation=75)
plt.title("Top 10 Jogos por Receita Estimada")
plt.ylabel("Receita Estimada")
plt.tight_layout()
plt.savefig("grafico_receita.png")
plt.close()

# Gráfico 2 – Notas dos jogos
plt.figure(figsize=(10, 6))
plt.bar(df_sorted_nota["titulo"], df_sorted_nota["nota"])
plt.xticks(rotation=75)
plt.title("Notas dos Jogos")
plt.ylabel("Nota")
plt.tight_layout()
plt.savefig("grafico_notas.png")
plt.close()

# Gráfico 3 – Média por gênero
plt.figure(figsize=(10, 6))
plt.bar(metricas_genero.index, metricas_genero["nota"])
plt.title("Média de Notas por Gênero")
plt.ylabel("Nota Média")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_genero_nota.png")
plt.close()

print("ETL concluído com sucesso!")
print("- games_transformado.csv gerado")
print("- grafico_receita.png")
print("- grafico_notas.png")
print("- grafico_genero_nota.png")
print("\nMétricas por gênero:\n", metricas_genero)
