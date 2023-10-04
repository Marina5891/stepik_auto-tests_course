from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # Ожидаем, пока цена не станер равна $100
  price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )

  # Получаем ссылку на кнопку Book и жмякаем на нее
  book_button = browser.find_element(By.ID, "book")
  book_button.click()

  # Получаем переменную и расчитываем результат по формуле 
  x = browser.find_element(By.ID, "input_value").text
  x_element = calc(x)

  # Находим поле для ответа и вводим полученный результат
  input = browser.find_element(By.ID, "answer")
  input.send_keys(x_element)
  
  # Жмякаем на кнопку Submit
  button = browser.find_element(By.ID, "solve")
  button.click()

finally:
  time.sleep(10)
  browser.quit()
# Не забываем оставить пустую строку в конце файла