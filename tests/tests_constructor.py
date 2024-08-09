from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from settings import Data


class TestStellarConstructor:
    def test_from_buns_to_toppings(self, driver):
        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()
        element_toppings = driver.find_element(*Locators.STEP_ON_THE_TAB)
        assert element_toppings == element_toppings

    def test_from_buns_to_sauces(self, driver):
        constructor_sauces = driver.find_element(*Locators.CONSTRUCTOR_SAUCES)
        constructor_sauces.click()
        element_sauces = driver.find_element(*Locators.STEP_ON_THE_TAB)
        assert element_sauces == element_sauces

    def test_from_buns_to_toppings_and_back_to_buns(self, driver):
        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()
        constructor_buns = driver.find_element(*Locators.CONSTRUCTOR_BUNS)
        constructor_buns.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STEP_ON_THE_TAB))
        element_buns = driver.find_element(*Locators.STEP_ON_THE_TAB)
        assert element_buns == element_buns









