from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Записываем данные в поля ввода 
    input1 = browser.find_element(By.XPATH, "//input[@name='firstname' and @required]")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.XPATH, "//input[@name='lastname' and @required]")
    input2.send_keys("Ivanov")

    input3 = browser.find_element(By.XPATH, "//input[@name='email' and @required]")
    input3.send_keys("IvanIvanov@mail.ru")

    # Вычисляем результат функции calc
    file = browser.find_element(By.ID, "file")

    # Получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))   
    # Добавляем к этому пути имя файла   
    file_path = os.path.join(current_dir, 'file_lesson2-2_step8.txt')      
    # Загружаем файл     
    file.send_keys(file_path)
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:

    # Ожидаем, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()
# Не забываем оставить пустую строку в конце файла