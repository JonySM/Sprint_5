from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Settings


class TestStellarSwitchToConstructor:
    def test_switch_from_lk_to_constructor(self, driver):
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

        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.MAIN_TEXT))

        main_text = driver.find_element(*Locators.MAIN_TEXT)
        assert main_text.is_displayed()









