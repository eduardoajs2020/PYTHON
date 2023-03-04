from IPython.display import display
import requests
from bs4 import BeautifulSoup

url = "https://www.tjmg.jus.br"
search_word = "home"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

occurrences = soup.find_all(string=lambda text: search_word in text.lower())

print(f"Numero de ocorrencias de '{search_word}': {len(occurrences)}")
for occurrence in occurrences:
    print(f"Found '{search_word}' in: {occurrence.parent}")


    display(occurrences)

