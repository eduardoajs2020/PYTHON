"""""
Formatando valores com modificadores: 

:s - Texto (strings)
:d - Inteiros (Int)
:f - Números de ponto flutuante(Float) (.2f)

:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - ESQUERDA
< - DIREITA
^ - CENTRO

"""""

num1 = 14
num2 = 33

resultado = num2/num1

print()
print()
print(f'{resultado:.2f}')
print(f'{num2:.2f}')
print(f'{num1:0>10}')
print(f'{num1:0<10}')
print(f'{num1:#^20}')
print()
print()
nome = 'projeto_teste'

sobrenome = 'alcunha'
print(f'{nome:#>100}')
print(f'{nome:#<100}')
print(f'{nome:#^100}')
print()
print(len(nome))
nome_formatado = '{:@^50}'.format(nome)
#nome_formatado = '{n}{n}{n}{n}{n}{n}'.format(n=nome)

nome_formatado = '{0} {1}'.format(nome, sobrenome)
print()
print(nome_formatado)
print(nome_formatado.lower())
print(nome_formatado.upper())
print(nome_formatado.title())




