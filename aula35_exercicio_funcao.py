print('===========================Exercicio 1=================================')


def ola_mundo():
    return 'ola mundo'


def mestra(funcao):
    return funcao()


executando = mestra(ola_mundo)
print(executando)


print('===========================Exercicio 2=================================')


def mestra(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi{nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestra(fala_oi, ' Luiz')
executando2 = mestra(saudacao, ' Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)


print('===========================FIM=========================================')
