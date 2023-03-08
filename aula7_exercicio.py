nome = 'Eduardo'
altura = 1.70
peso = 79
ano_atual = 2023
ano_nascimento = 1979
idade = ano_atual-ano_nascimento
imc = peso/altura**2

print(f'{nome} nasceu em {ano_nascimento}, tem {idade} anos de idade em '
      f'{ano_atual}, sua altura e {altura}, seu peso e '
      f'{peso} e seu imc e {imc:.2f}')
