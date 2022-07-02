nome = 'Eduardo'
altura = 1.70
peso = 79
ano_atual = 2022
ano_nascimento = 1979
idade = ano_atual-ano_nascimento
imc = peso/altura**2

print(f'{nome} nasceu em {ano_nascimento}, tem {idade} anos de idade em '
      f'{ano_atual}, sua altura é {altura}, seu peso é '
      f'{peso} e seu imc é {imc:.2f}')
