import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html"
browser.get(link)
button = browser.find_element(By.ID, "button")
button.click()
time.sleep(10)
browser.quit()
