import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение х из текстового поля
    x_element = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")

    # Расчитываем ответ, который будет введен в input
    y = calc(x_element)

    # Получаем поле для ответа и вводим ответ
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Ставим галочку в чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем нужную радиокнопку
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла