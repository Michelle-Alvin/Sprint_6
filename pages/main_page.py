from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def scroll_to(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def cookie_bar_closer(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.COOKIE_BANNER)).click()

    def open_order_form(self, button=MainPageLocators.UPPER_ORDER_BUTTON):
        self.scroll_to(button)
        self.click(button)
