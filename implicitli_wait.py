from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    link = 'http://suninjuly.github.io/wait1.html'
    driver.get(link)
    driver.maximize_window()
    """Ищем элемент в течении 5 секунд"""
    driver.implicitly_wait(5) # Вводим неявног ожидания, которое не надо вводить какждый раз как time.sleep()
    button = driver.find_element(By.ID, 'verify')
    button.click()
    massage = driver.find_element(By.ID, 'verify_message')

    assert 'successful' in massage.text
    print('Test is good')

finally:
    print('The End')
    driver.close()
