from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        self.driver.get(self.url)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_input(self, locator, text):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.text

    def go_to_main(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    def go_to_dzen(self):
        self.click(BasePageLocators.YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
