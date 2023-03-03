import pandas as pd

# Lê o arquivo CSV
data = pd.read_csv('C:\\PROJETOS DEV\\PYTON\\PROCESSO_QUEBRA_DE_CAIXA.csv')

# Filtra as linhas para vendas realizadas no último trimestre
dados_mensais = data[data['out_21'] !=0]


# Escreve os dados filtrados em um novo arquivo CSV
dados_mensais.to_csv('C:\\PROJETOS DEV\\PYTON\\NOVO_PROCESSO_QUEBRA_DE_CAIXA.csv', index=False)
#print(dados_mensais)