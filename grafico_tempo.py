import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from datetime import datetime

dados_pastas = pd.read_csv('./data/dadosPastas.csv', sep=',')

# Configure o estilo do Seaborn (opcional, mas pode melhorar a estética)
sns.set(style="whitegrid")

# Crie uma figura com as dimensões desejadas (2000x1000 pixels)
fig, ax = plt.subplots(figsize=(20, 10))

# Configure o formato de data no eixo x
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_major_locator(mdates.YearLocator())

# Lista para armazenar os rótulos das barras
rotulos_barras = []

# Itere sobre os dados das pastas e plote as barras horizontais
for i, pasta in enumerate(dados_pastas.itertuples()):
    if pd.notna(pasta.inicio_ano) and pd.notna(pasta.fim_ano):
        inicio = datetime.strptime(str(int(pasta.inicio_ano)), "%Y")
        fim = datetime.strptime(str(int(pasta.fim_ano)), "%Y")
        duracao = fim - inicio
        sigla_estado = pasta.Tipo_de_arquivo.split("/")[4]
        rotulos_barras.append(sigla_estado)
        # Use o Matplotlib para criar as barras horizontais
        ax.barh(sigla_estado, duracao, left=inicio)

# Configure os limites do eixo x
ax.set_xlim(datetime(1958, 1, 1), datetime(2024, 1, 1))

# Ajuste os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Configure o título e os rótulos dos eixos
plt.title("Linhas do Tempo das Pastas")
plt.xlabel("Ano")
plt.ylabel("Pastas")

# Salvar o gráfico como uma imagem SVG
plt.savefig("img/grafico_pastas_seaborn.svg", format="svg")

# Exiba o gráfico
plt.show()
