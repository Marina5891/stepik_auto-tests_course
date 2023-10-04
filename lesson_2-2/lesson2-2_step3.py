from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

link = "http://suninjuly.github.io/selects2.html"

def sum(a, b):
    return str(int(a) + int(b))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем из верстки переменные 
    number_1 = browser.find_element(By.ID, 'num1')
    number_2 = browser.find_element(By.ID, 'num2')

    # Вычисляем сумму полученных переменных
    summary = sum(number_1.text, number_2.text)

    # Ищем в select полученное значение
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(f"{summary}") 

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:

    # Ожидаем, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
# Не забываем оставить пустую строку в конце файла