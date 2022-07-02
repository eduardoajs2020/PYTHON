usuario = input('Digite seu primeiro nome: ')
qtd_caracteres = len(usuario)

if qtd_caracteres <= 4:
    print('O seu nome é muito curto!')
elif 5 >= qtd_caracteres <= 6:
    print('O seu nome é normal!')
else:
    print('O seu nome é muito grande!')
