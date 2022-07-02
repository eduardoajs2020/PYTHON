import selenium as selenium
from selenium.webdriver import firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

with selenium.webdriver.firefox as driver:

    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    assert isinstance(driver.find_element(By.NAME, "q").send_keys, object)
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
    print(first_result.get_attribute("textContent"))
