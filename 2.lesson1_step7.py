from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
try:
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, 'img')
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.ID, "robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.ID, "robotsRule")
    button2.click()
    button3 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button3.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
