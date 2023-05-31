from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
try:
    browser.get(link)

    x = browser.find_element(By.ID, 'num1')
    y = browser.find_element(By.ID, 'num2')
    answer = int(x.text) + int(y.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))
    button3 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button3.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

