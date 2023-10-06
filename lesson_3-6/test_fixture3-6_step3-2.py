import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        time.sleep(3)
        # этот тест запустится 2 раза
        def test_guest_should_see_navbar_element(self, browser, language):
        # этот тест тоже запустится дважды
            pass