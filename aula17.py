"""""
Aula 8 - while/else
"""""

contador = 1
acumulador = 1

while contador <= 1000:
    acumulador = acumulador + contador
    contador += 1
# if contador > 50:
#     break
    print(contador, acumulador)
else:
    print('Fim da lista!')
