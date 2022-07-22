variavel = 'valor'  # Escopo global


def func():
    print(variavel)


def func2():
    # global variavel
    variavel = 'Outro valor'  # Escopo local
    print(variavel)


func()  # global
func2()  # local
print(variavel)  # global



print('=========================================================================')


variavel = 'valor'  # Escopo global


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg



func()
outra_variavel = func2(arg=variavel)
func2(arg=variavel)

print(outra_variavel)


print('=========================================================================')
