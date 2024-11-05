import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")

    num1 = driver.find_element(By.ID, 'num1').text
    print(num1)
    num2 = driver.find_element(By.ID, 'num2').text
    print(num2)
    sum_num = int(num1) + int(num2)
    print(sum_num)


    select = Select(driver.find_element(By.TAG_NAME, "select")) # создаем переменную и вписываем в нее выпадающий список
    select.select_by_value(str(sum_num)) # Возвращаем из выпадающего списка число которое получилось при складывании
    print('OGO!')

    submit_btn =  driver.find_element(By.XPATH, '//button[@type="submit"]').click()


finally:
    time.sleep(5)
    driver.quit()