from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Settings


class TestStellarLK:
    def test_switch_to_lk(self, driver):
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

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON_INSIDE_LK))

        logout_button = driver.find_element(*Locators.LOGOUT_BUTTON_INSIDE_LK)
        assert logout_button.is_displayed()







