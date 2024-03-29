
# FERRAMENTA: AUTOMATIZADOR DO MOUSE, TECLADO E A TELA (BIBLIOTECA: PYAUTOGUI) = !pip install pyautogui

import pyautogui
import pyperclip
import pyperclip # Copiar e colar o texto
import time  # espera somente na primeira linha
import pandas  # copiar bases de dados para

pyautogui.PAUSE = 1  # tempo de espera entre comandos

# 1) Entrar no sistema da empresa(pasta do google drive(link))


pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# pyautogui.write ("usuario", "cxxx") -> usuario e senha
# pyautogui.write ("senha", "*****") -> usuario e senha

#site carregando...
time.sleep(5)


# 2) Navegar no sistema e encontrar a base de dados(link)
pyautogui.click(x=1073, y=725, clicks=2)  # time.sleep(5)
time.sleep(2)

# 3) Download da base de dados
pyautogui.click(x=1074, y=842)  # clicou no arquivo
pyautogui.click(x=3265, y=725)  # clicou nos 3 pontos
pyautogui.click(x=2773, y=1527)  # fazer download
time.sleep(7)

# pyautogui.scroll(100) = rolar tela

#4) Calcular os Indicadores(faturamento, quantidade de produtos

tabela = pandas.read_excel(r'C:\downloads\Vendas - Dez.xlsx')
print(tabela)


quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor final'].sum()

print(quantidade)
print(faturamento)

#5) Entrar no email

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(7)


#6) mandar um email para a diretoria com os indicadores.

# clicar no botão +
pyautogui.click(x=84, y=32)

# escrever o destinatário
pyautogui.write("maxer_tl@hotmail.com")
pyautogui.press("tab")  # seleciona o email
pyautogui.press("tab")  # passa para o campo de assunto

#escrever o assunto
pyperclip.copy("Relatorio de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")  # passa para o corpo de email

#escrever corpo do email
texto = f""" Prezados, bom dia.

O Faturamento foi de R$ {faturamento:,.2f}
A quantidade de produtos foi de:{quantidade:,}

Abs

Lira Python
"""

pyperclip.copy("texto")
pyautogui.hotkey("ctrl", "v")


#anexar arquivo

#enviar o email
pyautogui.hotkey("ctrl", "enter")

