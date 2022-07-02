usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar no mínimo 6 caracteres')
else:
    print('Usuario logado com sucesso!')
