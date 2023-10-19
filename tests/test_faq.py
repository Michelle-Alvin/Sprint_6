import pytest
from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestFAQ:
    @pytest.mark.parametrize("question, answer", [
        [BasePageLocators.PRICE_QUESTION, BasePageLocators.PRICE_ANSWER],
        [BasePageLocators.FEW_SCOOTER_QUESTION, BasePageLocators.FEW_SCOOTER_ANSWER],
        [BasePageLocators.RENT_TIME_QUESTION, BasePageLocators.RENT_TIME_ANSWER],
        [BasePageLocators.TODAY_ORDER_QUESTION, BasePageLocators.TODAY_ORDER_ANSWER],
        [BasePageLocators.DURATION_ORDER_QUESTION, BasePageLocators.DURATION_ORDER_ANSWER],
        [BasePageLocators.CHARGER_QUESTION, BasePageLocators.CHARGER_ANSWER],
        [BasePageLocators.CANCEL_QUESTION, BasePageLocators.CANCEL_ANSWER],
        [BasePageLocators.COUNTRYSIDE_QUESTION, BasePageLocators.COUNTRYSIDE_ANSWER]
                                                  ])
    def test_display_accordion(self, driver, question, answer):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        element = driver.find_element(*question)

        driver.execute_script("arguments[0].scrollIntoView();", element)
        element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(question))
        element.click()