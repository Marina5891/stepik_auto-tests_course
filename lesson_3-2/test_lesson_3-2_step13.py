from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestsSuccessAndError(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_1_success(self):
        browser = self.browser
        browser.implicitly_wait(2)
        browser.get("http://suninjuly.github.io/registration1.html")

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

        # Закрываем браузер
        browser.quit()

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome, welcome_text, "Тексты сообщений не совпадают")
        

    def test_2_error(self):
        browser = self.browser
        browser.implicitly_wait(2)
        browser.get("http://suninjuly.github.io/registration2.html")

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

        # Закрываем браузер
        browser.quit()

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome, welcome_text, "Тексты сообщений не совпадают")

if __name__ == "__main__":
    unittest.main()
