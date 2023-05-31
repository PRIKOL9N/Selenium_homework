import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '../file.txt')           # добавляем к этому пути имя файла
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
inputs = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
for answer in inputs:
    answer.send_keys("dabda")
upload = browser.find_element(By.ID, "file")
upload.send_keys(file_path)
button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
time.sleep(10)
browser.quit()
