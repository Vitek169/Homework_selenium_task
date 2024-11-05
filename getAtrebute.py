from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.XPATH, '//img[@id="treasure"]')
    x = x_element.get_attribute('valuex') # Получаем числоБ которое спрятано в втребуте valuex
    print(x)
    y = calc(x)
    input_text = driver.find_element(By.XPATH, '//input[@id="answer"]')
    input_text.send_keys(y)
    print(y)

    check_input = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    radio_ibput = driver.find_element(By.XPATH,'//input[@id="robotsRule"]').click()
    submit_button = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    print('End Test')



finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()



