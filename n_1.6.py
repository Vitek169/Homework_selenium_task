from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/registration1.html')

    first_name = driver.find_element(By.XPATH,'//input[@placeholder="Input your first name"]')
    first_name.send_keys('Ivan')

    last_name = driver.find_element(By.XPATH,'//input[@placeholder="Input your last name"]')
    last_name.send_keys('Ivanov')

    email = driver.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    email.send_keys('Ivanov@gmail.com')

    submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_btn.click()

    welcome_text_bilboard = driver.find_element(By.XPATH, '//div[@class="container"]')
    welcom_text = 'Congratulations! You have successfully registered!'

    assert welcom_text == welcome_text_bilboard.text
    print('Test is good')

finally:
    time.sleep(1)
    driver.quit()


