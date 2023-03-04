from IPython.display import display
import requests
from bs4 import BeautifulSoup
from pathlib import Path



#URL da página que queremos analisar
url = 'https://www.tjmg.jus.br'

#Faz o download da página
response = requests.get(url)

#Analisa o conteúdo HTML usando o BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#Busca a palavra informada no conteúdo da página
palavra1 = 'processo'
palavra2 = 'processos'
        
texto = soup.get_text().lower()

#Conta quantas vezes a palavra aparece no texto 
frequencia1 = texto.count(palavra1) 
frequencia2= texto.count(palavra2) 

if frequencia1 > 0 or frequencia2 > 0:

    print(f"A palavra {palavra1} foi encontrada {frequencia1} vezes e a palavra {palavra2} foi encontrada {frequencia2} vezes na página.")

#Exibe a palavra todas as vezes em que ela apareceu na url
    for i in range(frequencia1):

        print(f"{palavra1}\n")

        for i in range(frequencia2):

         print(f"{palavra2}\n")

#Cria o arquivo para armazenar os dados(txt ou csv)
    caminho = Path('arquivo_0.txt')

    caminho.touch(exist_ok=True)



# Abre o arquivo em modo de escrita
    with open('arquivo_0.txt', 'w') as arquivo:
        for i in range(frequencia1):
            print(f"{palavra1}\n")
            arquivo.write(palavra1 + ','+'\n')  # escreve a palavra1 no arquivo

        for i in range(frequencia2):
            print(f"{palavra2}\n")
            arquivo.write(palavra2 +','+'\n')  # escreve a palavra2 no arquivo

# Abre o arquivo em modo de Leitura
    with open('arquivo_0.txt', 'r') as arquivo:
        for linha in arquivo:
            if palavra1 in linha and palavra2 in linha:
                print(linha)

else:

    print(f"A palavra {palavra1} e/ou a palavra {palavra2} não foram encontradas na página.")



