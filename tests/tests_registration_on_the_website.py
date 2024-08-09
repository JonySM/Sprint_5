from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import Help
from locators import Locators
from settings import Data


class TestStellarRegistration:
    def test_success_registration(self, driver):
        login_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_button.click()
        registration_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()
        registration_name = driver.find_element(*Locators.REGISTRATION_NAME_FILD)
        registration_name.send_keys(Help.generated_name())
        registration_email = driver.find_element(*Locators.REGISTRATION_EMAIL_FILD)
        registration_email.send_keys(Help.generated_email())
        registration_password = driver.find_element(*Locators.REGISTRATION_PASSWORD_FILD)
        registration_password.send_keys(Help.generated_password())
        registration_main_button = driver.find_element(*Locators.REGISTRATION_MAIN_BUTTON)
        registration_main_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.MAIN_LOGIN_TEXT))
        main_login_text = driver.find_element(*Locators.MAIN_LOGIN_TEXT)
        assert main_login_text.is_displayed()

    def test_registration_with_invalid_password(self, driver):
        login_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_button.click()
        registration_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()
        registration_name = driver.find_element(*Locators.REGISTRATION_NAME_FILD)
        registration_name.send_keys(Help.generated_name())
        registration_email = driver.find_element(*Locators.REGISTRATION_EMAIL_FILD)
        registration_email.send_keys(Help.generated_email())
        invalid_password = driver.find_element(*Locators.REGISTRATION_PASSWORD_FILD)
        invalid_password.send_keys(Help.generated_invalid_password())
        registration_main_button = driver.find_element(*Locators.REGISTRATION_MAIN_BUTTON)
        registration_main_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
        error_text = driver.find_element(*Locators.ERROR_TEXT)
        assert error_text.is_displayed()















