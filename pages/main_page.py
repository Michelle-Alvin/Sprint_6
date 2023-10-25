from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):

    @allure.step('Закрываем баннер с кукки')
    def cookie_bar_closer(self):
        self.click(BasePageLocators.COOKIE_BANNER)

    @allure.step('Открываем форму заказа самоката')
    def open_order_form(self, button=MainPageLocators.UPPER_ORDER_BUTTON):
        self.scroll_to(button)
        self.click(button)

    @allure.step('Переходим на главную страницу через "Самокат"')
    def go_to_main(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Переходим на страницу "Дзен" через лого "Яндекс"')
    def go_to_dzen(self):
        self.click(BasePageLocators.YANDEX_LOGO)
        self.open_new_tab("https://dzen.ru/?yredirect=true")
