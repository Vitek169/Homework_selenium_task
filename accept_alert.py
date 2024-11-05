import math
import time
from selenium.webdriver.common.by import By
from selenium import  webdriver



"""Функция для посчета"""
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    driver = webdriver.Chrome()
    driver.get(link)

    """Нажимаем кнопку"""
    button_text = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_text.click()

    """Принимаем алерт"""
    alert_2 = driver.switch_to.alert # перекючаем на алерт
    print(alert_2.text)
    alert_2.accept() # принимаем алерт

    """Получаем число, которое ппредлагает программа"""
    window_input = driver.find_element(By.XPATH, '//input[@id="answer"]')
    x_1 = driver.find_element(By.XPATH, '//span[@id="input_value"]').text
    print('OK')
    """Считаем число которое появляеися"""
    y = calc(x_1)
    window_input.send_keys(y)
    print(y)

    button_2 = driver.find_element(By.XPATH,'//button[@type="submit"]')
    button_2.click()

    alert = driver.switch_to.alert
    print(alert.text)



finally:
    time.sleep(1)
    driver.quit()



