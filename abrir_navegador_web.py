import selenium
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

driver = Edge()

wait = WebDriverWait(driver, 10)
driver.get("https://google.com/ncr")
assert isinstance(driver.find_element(By.NAME, "q"), selenium.webdriver.remote.webelement.WebElement)
driver.find_element(By.NAME, "q").send_keys("provas SEF MG" + Keys.RETURN)
first_result = wait.until(
    presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
print(first_result.get_attribute("textContent"))

driver.quit()
