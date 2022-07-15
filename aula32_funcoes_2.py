print('=================================exercicio 1=======================')


def saudar(tipo, nome):

    return tipo, nome


saudacao = saudar('Olá', 'Eduardo')
if saudacao:
    print('Resultado = ', saudacao)
else:
    print('Texto inválido')


print('=================================exercicio 2=======================')


def somar(num1, num2, num3):

    return num1 + num2 + num3


soma = somar(10, 20, 12)
if soma:
    print('Resultado = ', soma)
else:
    print('Conta inválida')


print('=================================exercicio 3=======================')


def module(valor, percentual):
    return valor + valor * percentual/100




calculo = module(10, 20)

if calculo:
    print('Resultado = ', calculo)
else:
    print('Conta inválida')

print('=================================exercicio 4=======================')


def numero(valor):

    if valor % 3 == 0 and valor % 5 == 0:
        return 'Fizzbuzz'

    if valor % 3 == 0:
        return'Fizz'

    if valor % 5 == 0:
        return'buzz'
    else:
        return valor


print(numero(7))
print(numero(9))
print(numero(10))
print(numero(15))


print('=================================FIM===============================')

