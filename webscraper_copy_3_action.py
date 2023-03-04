from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

navegador = webdriver.Edge()

# navega para uma página que requer scroll
navegador.get('https://www.tjmg.jus.br/portal-tjmg/processos/andamento-processual/#.ZANXnBXMLrc')

# encontra o elemento que deve ser clicado
elemento = navegador.find_element(
    'xpath', '/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[1]/select')

# utiliza o ActionChains para mover para o elemento e clicá-lo
ActionChains(navegador).move_to_element(elemento).click().perform()

# realiza o scroll na página
ActionChains(navegador).move_to_element(elemento).perform()
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
navegador.find_element('xpath','/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[1]/select').send_keys("parte")

ActionChains(navegador).move_to_element(elemento).perform()
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
navegador.find_element('xpath','/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[3]/div/select').send_keys("Belo Horizonte")


ActionChains(navegador).move_to_element(elemento).perform()
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
navegador.find_element('xpath','/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[4]/div/input[1]').send_keys("Celio Silva")

#navegador.implicitly_wait(5)

navegador.find_element(
    'xpath', '/html/body/div[1]/main/div[2]/div/div/div/div/article/div[2]/section[1]/div/div/div/div[1]/form/div[6]/button').send_keys(Keys.ENTER)

#navegador.implicitly_wait(5)

try:
    consulta_processo = navegador.find_element('xpath','/html/body/table[2]')
except:
    consulta_processo = navegador.find_element('xpath', '/html/body/p[4]')


print(consulta_processo.text)

#navegador.implicitly_wait(5)

# fecha o navegador
navegador.quit()
