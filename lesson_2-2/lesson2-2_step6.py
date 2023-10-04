from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем из верстки переменную 
    number = browser.find_element(By.ID, 'input_value').text

    # Вычисляем результат функции calc
    result = calc(number)

    button = browser.find_element(By.TAG_NAME, "button")
    

    # Ищем поле для ответа и вводим результат вычислений
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)
    
    # Отмечаем чекбокс галочкой
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # Выбираем радиокнопку с текстом "Robots rule"
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click() 

    button.click()

finally:

    # Ожидаем, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
# Не забываем оставить пустую строку в конце файла