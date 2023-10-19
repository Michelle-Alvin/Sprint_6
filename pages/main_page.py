from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def scroll_to(self, driver, locator):
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, driver, locator):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        return element.text
