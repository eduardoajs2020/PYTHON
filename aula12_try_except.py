num1 = input('Digite um número: ')
num2 = input('Digite outro numero: ')

try:

    num1 = float(num1)
    num2 = float(num2)

    print(f'A soma é: {num1 + num2}')

except:
    print('ERRO! ')
    print('Você precisa digitar um número válido! ')


