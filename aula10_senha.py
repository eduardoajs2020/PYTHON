usuario = input('Nome de usuário: ')
senha = input('Senha do usuário:')

usuario_bd = 'eduardo'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está Logado no sistema!')
else:
    print('usuário e senha inválidos!')
