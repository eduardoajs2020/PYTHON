from selenium import webdriver
from selenium.webdriver.common.keys import Keys


navegador = webdriver.ChromiumEdge()

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("consulta de processo")
#navegador.find_element('xpath', '/html/body/div[7]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3').send_keys("consulta de processo")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
navegador.find_element('xpath', '/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[1]/select').send_keys("parte")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
navegador.find_element('xpath', '/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[3]/div/select').send_keys("Belo Horizonte")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
navegador.find_element('xpath', '/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[4]/div/input[1]').send_keys("Eduardo Souza")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

consulta_processo = navegador.find_element('xpath','/html/body/table[2]').text

print(consulta_processo)