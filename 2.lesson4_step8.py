from math import log, sin
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(log(abs(12*sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
wait = browser.find_element(By.ID, "price")
button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button.click()
x = browser.find_element(By.ID, 'input_value')
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(calc(x.text))
button1 = browser.find_element(By.ID, 'solve')
button1.click()
time.sleep(10)
browser.quit()
