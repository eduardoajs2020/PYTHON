# indices
# 0123456789 .............33

frase = 'o rato roeu a roupa do rei de roma, a rainha ruim resolveu remendar'  # iteravel
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

# iteração <- iterar

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

    print(nova_string)
