hora = input('Que horas são? ')
try:
    hora = int(hora)
except:
    print('ERRO')

if 0 <= hora <= 11:
    print('Bom dia!')
elif 12 <= hora <= 17:
    print('Boa Tarde!')
elif 18 <= hora <= 23:
    print('Boa Noite!')
else:
    print('Hora inválida !')
