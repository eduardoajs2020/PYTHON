import pandas as pd

# Ler os dados dos arquivos CSV
dados1 = pd.read_csv('arquivo_0.csv')
dados2 = pd.read_csv('arquivo1.csv')

# Comparar os dados das duas tabelas
dados_repetidos = pd.merge(dados1, dados2, how='inner')

# Contar a quantidade de vezes que cada dado repetido aparece
contador = dados_repetidos.groupby(list(dados_repetidos.columns)).size().reset_index(name='ocorrencias')

# Escrever os dados repetidos em um arquivo CSV
contador.to_csv('dados_repetidos.txt', index=False)