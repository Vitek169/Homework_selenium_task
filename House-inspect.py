import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(link)
    driver.maximize_window()

    """Ожидание кликабельности"""
    price = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button_buy = driver.find_element(By.ID, 'book').click()
    print('OK')


    x = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    input_text= driver.find_element(By.XPATH, '//input[@id="answer"]')
    print(x)
    y = calc(x.text)
    print(y)
    input_text.send_keys(y)
    submit_button = driver.find_element(By.XPATH, '//button[@id="solve"]').click()

    alert_1 = driver.switch_to.alert.text
    print(alert_1)


finally:
    driver.quit()