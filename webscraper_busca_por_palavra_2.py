from IPython.display import display
import requests
import csv
from bs4 import BeautifulSoup
from pathlib import Path

# URL da página que queremos analisar
url = 'https://www.tjmg.jus.br'

# Faz o download da página
response = requests.get(url)

# Analisa o conteúdo HTML usando o BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Busca as palavras informadas no conteúdo da página
palavra1 = 'processo'
palavra2 = 'advogado'

texto = soup.get_text().lower()

# Conta quantas vezes cada palavra aparece no texto
frequencia1 = texto.count(palavra1)
frequencia2 = texto.count(palavra2)

if frequencia1 > 0 or frequencia2 > 0:

    print(
        f"A palavra '{palavra1}' foi encontrada {frequencia1} vezes na página.")
    print(
        f"A palavra '{palavra2}' foi encontrada {frequencia2} vezes na página.")

    # Cria o arquivo para armazenar os dados (CSV)
    caminho = Path('arquivo1.csv')

    # Abre o arquivo em modo de escrita
    with open('arquivo1.csv', 'w') as arquivo:
        # Escreve o cabeçalho das colunas
        arquivo.write(f"Palavra 1; Palavra 2\n")

        # Escreve as palavras e as frequências em colunas diferentes
        for i in range(frequencia1):
            linha = f"{palavra1};\n"
            arquivo.write(linha)
        for i in range(frequencia2):
            linha = f";{palavra2}\n"
            arquivo.write(linha)

    # Abre o arquivo em modo de leitura e exibe o conteúdo
    with open('arquivo1.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter='\t', quoting=csv.QUOTE_NONE)
        for linha in leitor_csv:
            if palavra1 and palavra2 in linha:
             print(linha)

else:
    print(
        f"As palavras '{palavra1}' e/ou '{palavra2}' não foram encontradas na página.")
