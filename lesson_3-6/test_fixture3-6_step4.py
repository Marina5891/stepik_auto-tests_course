from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import math

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    # Находим кнопку входа и нажимаем ее
    button_login = browser.find_element(By.CSS_SELECTOR, "#ember33")
    button_login.click()

    # Заполняем поля электронной почты и пароля
    email = WebDriverWait(browser, 3).until(
         EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    email.send_keys("почта")

    password = WebDriverWait(browser, 3).until(
         EC.visibility_of_element_located((By.ID, "id_login_password"))
    )
    password.send_keys("пароль")


    # Находим и нажимаем кнопку входа на форме авторизации
    button_ok = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader ")
    button_ok.click()

    # Высчитываем ответ
    answer = math.log(int(time.time()))
    time.sleep(10)

    # Находим поле для ввода ответа.
    # Очищаем поле
    # Записываем в текстовое поле ответ
    textarea = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.TAG_NAME, "textarea"))
    )
    textarea.clear()
    textarea.send_keys(answer)

    # Находим кнопку для отправки ответа и нажимаем ее
    button_answer = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission"))
    )
    button_answer.click()

    # Получаем текст сообщения
    message = WebDriverWait(browser, 25).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text

    # Сравниваем текст сообщения с правильным текстом
    assert "Correct!" == message, message