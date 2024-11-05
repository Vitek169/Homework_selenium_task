import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    print(x)
    y = calc(x)
    input_text = driver.find_element(By.XPATH, '//input[@id="answer"]')
    input_text.send_keys(y)
    print(y)

    driver.execute_script("window.scrollBy(0, 150);")
    check_input = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    driver.execute_script("window.scrollBy(0, 150);")
    radio_ibput = driver.find_element(By.XPATH,'//input[@id="robotsRule"]').click()
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("window.scrollBy(0, 150);") # скроллим на 150 икселей вниз
    submit_button.click()
    print('End Test')



finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()


