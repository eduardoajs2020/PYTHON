def saudacao(msg='Olá', nome='Sandro'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao()
saudacao('Ola pessoa', 'Eduardo')
saudacao('Oi', 'José')
saudacao('Hello', 'Maria')
saudacao('Ola', 'Otávio')
saudacao('Hi', 'João')

print('===============================================Funcoes DEF 2=====================')


def funcao(var):
    return var
    print('isso não sera executado.')


variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

print('=======================================Divisão=============================')


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 2)
if divide:
    print('Resultado = ', divide)
else:
    print('Conta inválida')

print('=======================================Divisão=============================')