print('=================================LAMBDA==========================')

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[0], reverse=True))
print(sorted(lista, key=lambda i: i[0], reverse=False))

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(sorted(lista, key=lambda i: i[1], reverse=False))
print(lista)

print('=================================LAMBDA2==========================')

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


lista.sort(key=func)

#print(sorted(lista, key=lambda i: i[0], reverse=True))
print(lista)


print('==============================COMUM===============================================')


def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)

print('=================================LAMBDA==========================')

a = lambda x, y: x * y

print(a(2, 2))


print('=================================FIM==========================')