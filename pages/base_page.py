from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def cookie_bar_closer(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BasePageLocators.COOKIE_BANNER)).click()
        return driver

    def click(self, driver, locator):
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()