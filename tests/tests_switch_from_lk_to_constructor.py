from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Data


class TestStellarSwitchToConstructor:
    def test_switch_from_lk_to_constructor(self, driver, authorization):
        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.MAIN_TEXT))
        main_text = driver.find_element(*Locators.MAIN_TEXT)
        assert main_text.is_displayed()
