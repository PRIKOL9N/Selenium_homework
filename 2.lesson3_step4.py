import os
from math import log, sin
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(log(abs(12*sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
x = browser.find_element(By.ID, 'input_value')
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(calc(x.text))
button1 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button1.click()
time.sleep(10)
browser.quit()
