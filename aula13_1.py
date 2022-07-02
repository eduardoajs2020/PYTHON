numero = input('Digite um número:')

if not numero.isdigit():
    print('ERRO')
    print('Você precisa digitar um número válido! ')

else:
    numero = int(numero)
if numero % 2 == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é impar!')

