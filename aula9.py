#Operadores lógicos são: and, or, not, (in e not in(não existe em)).

print('Digite um número qualquer: ')
numero = input()

if int(numero) > int(0):
    print(int(numero), 'é positivo.')
elif int(numero) < int(0):
    print(int(numero), 'é negativo.')
elif int(numero) == int(0):
    print(int(numero), 'é zero.')
else:
    print(numero, 'Digite um numero válido!')
