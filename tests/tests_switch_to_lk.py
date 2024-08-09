from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Data


class TestStellarLK:
    def test_switch_to_lk(self, driver, authorization):
        l_k_button = driver.find_element(*Locators.L_K_BUTTON)
        l_k_button.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON_INSIDE_LK))
        logout_button = driver.find_element(*Locators.LOGOUT_BUTTON_INSIDE_LK)
        assert logout_button.is_displayed()







