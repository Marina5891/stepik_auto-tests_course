from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмякаем на кнопку, чтобы перейти дальше
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

    # В выпавшем окне нажимаем на ОК
    confirm = browser.switch_to.alert
    confirm.accept()

    # Получаем переменную и расчитываем результат по формуле 
    x = browser.find_element(By.ID, "input_value").text
    x_element = calc(x)

    # Находим поле для ответа и вводим полученный результат
    input = browser.find_element(By.ID, "answer")
    input.send_keys(x_element)
    
    # Жмякаем на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # Ожидаем, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
# Не забываем оставить пустую строку в конце файла