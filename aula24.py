"""
Desempacotamento de listas em Python
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, *n3, n4 = lista  # *n3 = cria outra lista com os valores restantes

print(n2, n3)  # imprime o restante dos valores da lista, exceto o ultimo

print(n4)  # imprime o ultimo valor da lista
