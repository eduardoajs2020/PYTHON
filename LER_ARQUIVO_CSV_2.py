import pandas as pd

# Ler os dados da tabela e do arquivo de texto
dados = pd.read_csv('arquivo_0.csv')
with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
palavras = texto.split()

# Comparar as palavras do arquivo de texto com a coluna 'coluna_da_tabela' da tabela
dados_repetidos = dados[dados['coluna_da_tabela'].isin(palavras)]

# Contar a quantidade de vezes que cada palavra repetida aparece
contador = dados_repetidos['coluna_da_tabela'].value_counts().reset_index(name='ocorrencias')

# Escrever as palavras repetidas em um arquivo TXT
with open('palavras_repetidas.txt', 'w') as arquivo:
    for index, row in contador.iterrows():
        arquivo.write(f'{row["index"]}: {row["ocorrencias"]}\n')

        # Abrir um arquivo CSV para gravar as ocorrências repetidas
arquivo_saida = open('ocorrencias_repetidas.csv', 'w')
arquivo_saida.write('Palavra, Ocorrências\n')

# Gravar as ocorrências repetidas no arquivo CSV
for palavra, ocorrencias in contador.items():
    arquivo_saida.write(f'{palavra}, {ocorrencias}\n')

# Fechar o arquivo CSV
arquivo_saida.close()