import time
from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(log(abs(12*sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.ID, "input_value").text
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(calc(x_element))
button1 = browser.find_element(By.ID, "robotCheckbox")
button1.click()
button2 = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
browser.quit()
