from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Открываем сайт')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Кликаем по элементу')
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Вводим "{text}"')
    def fill_input(self, locator, text):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    @allure.step('Проверяем текст')
    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.text

    @allure.step('Скроллим до элемента')
    def scroll_to(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
