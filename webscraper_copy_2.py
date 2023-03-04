from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# instanciando o navegador Edge
navegador = webdriver.Edge()

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("consulta de processo")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# espera até que a página da consulta seja carregada
navegador.implicitly_wait(5)

# selecionando o tipo de busca (parte)
elemento=navegador.find_element('xpath','/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[1]/select').send_keys("parte")
ActionChains(navegador).move_to_element(elemento).click().perform()
elemento=navegador.find_element('xpath','/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[3]/div/select').send_keys("Belo Horizonte")
ActionChains(navegador).move_to_element(elemento).click().perform()
elemento=navegador.find_element('xpath','/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[4]/div/input[1]').send_keys("Eduardo Souza")
ActionChains(navegador).move_to_element(elemento).click().perform()
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# espera até que a página com o resultado seja carregada
navegador.implicitly_wait(5)

# buscando o elemento que contém o número do processo
consulta_processo = navegador.find_element('xpath','//*[@id="processos"]/div[2]/div/div[1]/div[1]/h5')

print(consulta_processo.text)

# fechando o navegador
navegador.quit()
