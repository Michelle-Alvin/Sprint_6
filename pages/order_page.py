from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    def fill_name(self, text):
        self.fill_input(OrderPageLocators.NAME_INPUT, text)

    def fill_surname(self, text):
        self.fill_input(OrderPageLocators.SURNAME_INPUT, text)

    def fill_address(self, text):
        self.fill_input(OrderPageLocators.ADDRESS_INPUT, text)

    def fill_metro(self, text):
        self.click(OrderPageLocators.METRO_INPUT)
        self.fill_input(OrderPageLocators.METRO_INPUT, text)
        self.click((By.XPATH, f"//div[text()='{text}']"))

    def fill_phone(self, text):
        self.fill_input(OrderPageLocators.PHONE_INPUT, text)

    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_date(self, text):
        self.fill_input(OrderPageLocators.DATE_INPUT, text)
        self.fill_input(OrderPageLocators.DATE_INPUT, Keys.RETURN)

    def fill_rent(self, text):
        self.click(OrderPageLocators.RENT_TIME_INPUT)
        self.click((By.XPATH, f"//div[text()='{text}']"))

    def fill_color(self, text):
        self.click((By.XPATH, f"//label[contains(text(), '{text}')]"))

    def fill_comment(self, text):
        self.fill_input(OrderPageLocators.COMMENT_INPUT, text)

    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def click_accept_order(self):
        self.click(OrderPageLocators.ACCEPT_ORDER_BUTTON)

    def get_order_status(self):
        return self.get_text(OrderPageLocators.ORDER_STATUS)
