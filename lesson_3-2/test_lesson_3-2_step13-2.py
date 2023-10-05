from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def links_testing(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.get(link)

    try:
        # Код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
        input3.send_keys("zero-mail@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Находим элемент, содержащий текст и записываем его в переменную
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text

    finally:
        browser.quit()

welcome = "Congratulations! You have successfully registered!"

def test_1_success():
    assert welcome == links_testing("http://suninjuly.github.io/registration1.html")
    

def test_2_error():
    assert welcome == links_testing("http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
    pytest.main()
