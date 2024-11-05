import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from trio import open_file

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/file_input.html')

    first_name = driver.find_element(By.XPATH,'//input[@name="firstname"]')
    first_name.send_keys('Ivan')

    last_name = driver.find_element(By.XPATH,'//input[@name="lastname"]')
    last_name.send_keys('Ivanov')

    email = driver.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys('Ivanov@gmail.com')

    file_path =('/Users/katerinamatuizo/QA_Selenium/pythonProject/text.text')

    the_file_open = driver.find_element(By.XPATH,'//input[@id="file"]')
    the_file_open.send_keys(file_path)

    submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_btn.click()

    print('Test is good')

finally:
    time.sleep(25)
    driver.quit()