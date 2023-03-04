import requests
from bs4 import BeautifulSoup

# URL da página que queremos analisar
url = 'https://www.tjmg.jus.br'

# Faz o download da página
response = requests.get(url)

# Analisa o conteúdo HTML usando o BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Busca a palavra "python" no conteúdo da página
palavra = 'juizado'

if palavra in soup.get_text().lower():

    print (f"A palavra {palavra} foi encontrada {len(palavra)} vezes na pagina.")

else:

    print(f"A palavra {palavra} nao foi encontrada na pagina.")
