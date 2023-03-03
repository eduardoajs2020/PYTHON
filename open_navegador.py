from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = "C:/PROJETOS DEV/PYTON/venv/lib/site-packages/selenium/webdriver/chrome/service.py"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

s = Service(driver_path)
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(service=s, options=option)
browser.get("https://www.google.br")


