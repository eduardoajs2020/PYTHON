"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
"""
booleanos = True
inteiros = 10
flutuante = -10.10
strings = 'textos'

texto = 'valor'
lista = [1, 2, 3, 4, 'Luiz']

"""

#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# -      -5   -4   -3   -2   -1

lista[5] = 'Qualquer outra coisa'  # modifica valor do índice 5

print(lista[-1])  # mostra o ultimo elemento da lista
print(lista[0:2])  # fatia string(mostra intervalo < que 2)
print(lista[::])  # mostra todos os valores da lista
print(lista[::2])  # mostra os valores, pulando de 2 em 2
print(lista[::-1])  # mostra a lista invertida

print('========================INTERVALO============================')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2  # junta as listas

print(lista1)
print(lista2)
print(lista3)

print('====================FUNÇÃO=EXTEND=============================')

lista1.extend(lista2)  # expande a lista
print(lista1)
print(lista2)

print('====================FUNÇÃO=APPEND===============================')

lista1.append('append')  # adiciona elementos ao final da lista
print(lista1)
print(lista2)

print('====================FUNÇÃO=INSERT================================')

lista1.insert(0, 'insert')  # adiciona elementos ao índice citado da lista
print(lista1)
print(lista2)

print('====================FUNÇÃO=POP===================================')

lista1.pop()  # exclui elementos do índice citado da lista, ou, quando vazio, apaga o ultimo digitado!
print(lista1)

print('====================FUNÇÃO=DEL==================================')
# ÍNDICE  0  1  2  3  4  5  6  7  8
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del (lista4[3:5])  # exclui fatia da lista
print(lista4)

print('====================FUNÇÃO=MAX=MIN==============================')

print(max(lista4))  # Exibe máximo e mínimo da lista
print(min(lista4))

print('====================FUNÇÃO=RANGE=================================')

lista5 = range(1, 10)  # Cria um objeto iterável, não uma lista
print(lista5)

print('====================FUNÇÃO=RANGE=LIST============================')
lista5 = list(range(1, 10))  # Cria uma lista, a partir do objeto iteravel
print(lista5)

print('====================FUNÇÃO=RANGE=LIST=M==========================')
lista5 = list(range(0, 100, 8))  # Manipula o objeto range(neste caso, exibe de 8 em 8)
print(lista5)

print('==================FOR=NA=FUNÇÃO=RANGE=LIST=======================')
for valor in lista5:  # percorre o objeto range
    print(valor)

print('=========================FUNÇÃO=ELEMENT==========================')
lista6 = ['string', True, 10, -20.5]
for elem in lista6:  # exibe o tipo de cada elemento da lista
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

print('=========================FUNÇÃO=CLEAR==========================')
lista7 = list(range(10, 20))
print(lista7)

lista7.clear()

print(lista7)

lista7 = list(range(1, 13))
print(lista7)

print('=============IMPRIMIR=STRING=VAZIA==========================')
"""
texto_preenchido = 'script de teste'
texto_digitado = input('Digite uma palavra: ')

vazio_final = ''

for vazio_final in texto_digitado:
    if vazio_final in texto_digitado:
        texto_preenchido += vazio_final
    else:
        vazio_final += '*'
    print(texto_preenchido)
"""
print('=========================EXEMPLO=============================')

secreto = 'python'
secreto_temporario = ''

#digitadas = ['t']
digitadas = input('Digite uma letra: ')


for letra_secreta in secreto:

    if letra_secreta in digitadas:

        secreto_temporario += letra_secreta


    else:

        secreto_temporario += '*'

    print(secreto_temporario)

    if secreto == secreto_temporario:
        print('Você ganhou')
print('==============================FIM=============================')
