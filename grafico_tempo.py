import pandas as pd
import plotly.express as px

dados_pastas = pd.read_csv('./data/dadosPastas.csv', sep=',')

# Filtrar os dados para garantir que apenas os registros com valores de início e fim de ano sejam incluídos
dados_pastas = dados_pastas.dropna(subset=['inicio_ano', 'fim_ano'])

# Converter as colunas de início e fim de ano para o tipo de data
dados_pastas['inicio_ano'] = pd.to_datetime(dados_pastas['inicio_ano'], format='%Y')
dados_pastas['fim_ano'] = pd.to_datetime(dados_pastas['fim_ano'], format='%Y')

# Calcular a duração em anos
dados_pastas['duracao'] = (dados_pastas['fim_ano'] - dados_pastas['inicio_ano']).dt.days / 365

dados_txt = dados_pastas[dados_pastas['Tipo_de_arquivo'].str.contains('txt')]

# Criar o gráfico de linha do tempo com Plotly Express
fig = px.timeline(
    dados_txt,
    x_start='inicio_ano',
    x_end='fim_ano',
    y='Tipo_de_arquivo',
    color='Tipo_de_arquivo',
    labels={'inicio_ano': 'Início', 'fim_ano': 'Fim', 'duracao': 'Duração (Anos)'}
)

# Definir as dimensões da figura (2000x1000 pixels)
fig.update_layout(
    autosize=False,
    width=2000,
    height=1000
)

# Configurar o título
fig.update_layout(
    title="Linhas do Tempo das Pastas",
    xaxis_title="Ano",
    yaxis_title="Pastas"
)

# Salvar o gráfico como um arquivo PNG
fig.write_image("grafico_pastas.svg")
