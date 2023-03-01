from PySimpleGUI import PySimpleGUI as sg


#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario', size=(25,2))],
    [sg.Text('senha'),sg.Input(key='senha',password_char='*', size=(25,2))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de Login', layout)
#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Eduardo' and valores['senha'] == '123456':
            print('Bem vindo!')
    
