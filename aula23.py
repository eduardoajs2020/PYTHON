"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list #iteraveis
"""

from xmlrpc.client import boolean


string = "O Brasil é o pais do futebol, o Brasil é penta !"
string2 = "O Brasil é ruim de bola!"

lista1 = string.split()
print(lista1)
print('===================================================')

lista2 = string.upper()
print(lista2)
print('===================================================')

lista3 = string.title()
print(lista3)
print('===================================================')

lista4 = string.join(string2)
print(lista4)
print('===================================================')

for enumere in string2:
    print(enumere)

print('===================================================')

for enumere in enumerate(string2):
    print(enumere)
print('===================================================')

lista = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 0, 1, 1]]
enumer = list(enumerate(lista))

print(enumer)

print(enumer[0])
print(enumer[1])
print(enumer[2])


print('===================================================')
