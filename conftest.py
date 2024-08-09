import pytest
from selenium import webdriver
from locators import Locators
from settings import Url, Data


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Url.STELLAR_BURGERS_URL)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture
def authorization(driver):
    login_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
    login_button.click()
    email = driver.find_element(*Locators.LOGIN_INPUT_FIELD)
    email.send_keys(Data.AUTH_EMAIL)
    password = driver.find_element(*Locators.PASSWORD_INPUT_FIELD)
    password.send_keys(Data.AUTH_PASSWORD)
    login_main_button = driver.find_element(*Locators.LOGIN_MAIN_BUTTON)
    login_main_button.click()










