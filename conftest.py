import pytest
from selenium import webdriver
from settings import Settings


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Settings.STELLAR_BURGERS_URL)

    yield chrome_driver
    chrome_driver.quit()










