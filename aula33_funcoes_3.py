def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


func(1, 2, 3, 4, 5)

print('================================CAST==========================================')


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)

print('================================CAST 2=========================================')


def func(*args):
    for v in args:
        print(v)


func(1, 2, 3, 4, 5)

print('================================DESEMPACOTAR LISTA=========================================')


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
func(*lista)

print('================================DESEMPACOTAR LISTA 2=========================================')


def func(*args):
    print(args)
    print(args[0])


lista = [1, 2, 3, 4, 5]
func(*lista, 10, 20, 30, 40)

print('================================KWARGS()=========================================')


def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    nome = kwargs.get('nome')  # outra forma de exibição
    print(nome)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')


print('============================================================================')


def func(*args, **kwargs):
    print(args)
    print(kwargs['idade'])

    idade = kwargs.get('idade')  # outra forma de exibição

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)
