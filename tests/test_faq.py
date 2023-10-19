import pytest
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFAQ:
    @pytest.mark.parametrize("question, answer, answer_text", [
        [MainPageLocators.PRICE_QUESTION, MainPageLocators.PRICE_ANSWER, test_data.ACCORD_0],
        [MainPageLocators.FEW_SCOOTER_QUESTION, MainPageLocators.FEW_SCOOTER_ANSWER, test_data.ACCORD_1],
        [MainPageLocators.RENT_TIME_QUESTION, MainPageLocators.RENT_TIME_ANSWER, test_data.ACCORD_2],
        [MainPageLocators.TODAY_ORDER_QUESTION, MainPageLocators.TODAY_ORDER_ANSWER, test_data.ACCORD_3],
        [MainPageLocators.DURATION_ORDER_QUESTION, MainPageLocators.DURATION_ORDER_ANSWER, test_data.ACCORD_4],
        [MainPageLocators.CHARGER_QUESTION, MainPageLocators.CHARGER_ANSWER, test_data.ACCORD_5],
        [MainPageLocators.CANCEL_QUESTION, MainPageLocators.CANCEL_ANSWER, test_data.ACCORD_6],
        [MainPageLocators.COUNTRYSIDE_QUESTION, MainPageLocators.COUNTRYSIDE_ANSWER, test_data.ACCORD_7]
                                                  ])
    def test_display_accordion(self, driver, question, answer, answer_text):
        main = MainPage(driver, "https://qa-scooter.praktikum-services.ru/")
        main.open()
        main.cookie_bar_closer(driver)
        main.scroll_to(driver, question)
        main.click(driver, question)
        text = main.get_text(driver, answer)

        assert answer_text == text, f'Ожидаемый текст = {answer_text}, Полученный текст = {text}'
