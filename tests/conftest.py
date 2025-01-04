import time

import pytest
from selenium import webdriver

from locators.personal_account_locators import PersonalAccountLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage
from urls import LOGIN_PAGE


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function")
def order_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture(scope="function")
def account_page(driver):
    return PersonalAccountPage(driver)

@pytest.fixture(scope="function")
def password_page(driver):
    return PasswordRecoveryPage(driver)

@pytest.fixture
def login_account(driver):
    pa = PersonalAccountPage(driver)
    pa.open_url(LOGIN_PAGE)
    pa.add_text_to_element(PersonalAccountLocators.NAME_INPUT,'lotosmdiplom@yandex.ru')
    pa.add_text_to_element(PersonalAccountLocators.PASSWORD_INPUT,'asdfghjk')
    pa.click_to_element(PersonalAccountLocators.LOGIN_BUTTON)
    time.sleep(5)
