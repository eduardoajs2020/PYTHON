num1 = input('Digite o Primeiro numero: ')
num2 = input('Digite o Segundo numero: ')


num1 = float(num1)
num2 = float (num2)


resultado = float (num1*num2)

print(resultado)

if resultado >= 50:
    print('Tá quente Pacaray')

    if resultado < 10:
        print('tá esfriando..,')

else:
    print('Tá gelado bagarayy')

    for resultado in range(0, 100):
        print('O numero está dentro do esperado!')

        vazio = ''
        vazio = resultado
        resultado += num1

        print(vazio)