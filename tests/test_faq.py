import pytest
import test_data
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestFAQ:
    @allure.title(f'Проверка блока "Вопросы о важном"')
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
        main = MainPage(driver)
        main.open()
        main.cookie_bar_closer()
        main.scroll_to(question)
        main.click(question)
        text = main.get_text(answer)

        assert answer_text == text, f'Ожидаемый текст = {answer_text}, Полученный текст = {text}'
