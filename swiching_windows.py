import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



"""Функция для посчета"""
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    button_fly = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    print('button click')
    """запрашиваем все вкладки, переключаемся на вторую"""
    all_windows = driver.window_handles
    print(all_windows)
    window_2 = driver.window_handles[1]
    driver.switch_to.window(window_2)
    print('window switch')

    """работаем со второй вкладкой"""
    x = driver.find_element(By.XPATH, '//span[@id="input_value"]') #получаем число
    input_value = driver.find_element(By.XPATH, '//input[@id="answer"]')#получаем поле ввода
    print(x.text)
    y = calc(x.text)
    print(y)
    input_value.send_keys(y) #вводим в поле ввода полученную цифру
    print("Input")

    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()


finally:
    time.sleep(2)
    driver.close()