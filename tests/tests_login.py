from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Settings


class TestStellarLogin:
    def test_login_main_page(self, driver):
        login_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_button.click()

        email = driver.find_element(*Locators.LOGIN_INPUT_FIELD)
        email.send_keys(Settings.AUTH_EMAIL)

        password = driver.find_element(*Locators.PASSWORD_INPUT_FIELD)
        password.send_keys(Settings.AUTH_PASSWORD)

        login_main_button = driver.find_element(*Locators.LOGIN_MAIN_BUTTON)
        login_main_button.click()

        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.OUR_NAME_TEXT))

        our_name = driver.find_element(*Locators.OUR_NAME_TEXT)
        assert our_name.is_displayed()

    def test_login_from_lk_page(self, driver):
        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()

        email = driver.find_element(*Locators.LOGIN_INPUT_FIELD)
        email.send_keys(Settings.AUTH_EMAIL)

        password = driver.find_element(*Locators.PASSWORD_INPUT_FIELD)
        password.send_keys(Settings.AUTH_PASSWORD)

        login_main_button = driver.find_element(*Locators.LOGIN_MAIN_BUTTON)
        login_main_button.click()

        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.OUR_LOGIN_TEXT))

        our_name = driver.find_element(*Locators.OUR_LOGIN_TEXT)
        assert our_name.is_displayed()

    def test_login_from_registration_button(self, driver):
        login_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_button.click()

        registration_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()

        login_register_page = driver.find_element(*Locators.LOGIN_OPTIONAL_BUTTON)
        login_register_page.click()

        email = driver.find_element(*Locators.LOGIN_INPUT_FIELD)
        email.send_keys(Settings.AUTH_EMAIL)

        password = driver.find_element(*Locators.PASSWORD_INPUT_FIELD)
        password.send_keys(Settings.AUTH_PASSWORD)

        login_main_button = driver.find_element(*Locators.LOGIN_MAIN_BUTTON)
        login_main_button.click()

        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.OUR_LOGIN_TEXT))

        our_name = driver.find_element(*Locators.OUR_LOGIN_TEXT)
        assert our_name.is_displayed()

    def test_login_from_recovery_password_button(self, driver):
        login_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_button.click()

        recovery_button = driver.find_element(*Locators.RECOVERY_PASSWORD_BUTTON)
        recovery_button.click()

        login_register_page = driver.find_element(*Locators.LOGIN_OPTIONAL_BUTTON)
        login_register_page.click()

        email = driver.find_element(*Locators.LOGIN_INPUT_FIELD)
        email.send_keys(Settings.AUTH_EMAIL)

        password = driver.find_element(*Locators.PASSWORD_INPUT_FIELD)
        password.send_keys(Settings.AUTH_PASSWORD)

        login_main_button = driver.find_element(*Locators.LOGIN_MAIN_BUTTON)
        login_main_button.click()

        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.OUR_NAME_TEXT))

        our_name = driver.find_element(*Locators.OUR_NAME_TEXT)
        assert our_name.is_displayed()

















