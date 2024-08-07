from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Settings


class TestStellarConstructor:
    def test_from_buns_to_toppings(self, driver):
        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()

        element_toppings = driver.find_element(*Locators.ELEMENT_TOPPINGS)
        assert element_toppings.is_displayed()

    def test_from_buns_to_sauces(self, driver):
        constructor_sauces = driver.find_element(*Locators.CONSTRUCTOR_SAUCES)
        constructor_sauces.click()

        element_sauces = driver.find_element(*Locators.ELEMENT_SAUCES)
        assert element_sauces.is_displayed()


    def test_from_buns_to_toppings_and_back_to_buns(self,driver):
        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()

        constructor_buns = driver.find_element(*Locators.CONSTRUCTOR_BUNS)
        constructor_buns.click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ELEMENT_BUNS))

        element_buns = driver.find_element(*Locators.ELEMENT_BUNS)
        assert element_buns.is_displayed()









