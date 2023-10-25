import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


class TestOrderFlow:
    @allure.title('Проверка флоу заказа самоката')
    @pytest.mark.parametrize("button_order, name, surname, address, metro, phone, date, rent, color, comment", [
        [MainPageLocators.UPPER_ORDER_BUTTON, "Арсений", "Лукин", "ул. Пушкина 77А", "Черкизовская", "89991234567",
         "21.10.2023", "трое суток", "чёрный жемчуг", "жду самокат"],
        [MainPageLocators.BOTTOM_ORDER_BUTTON, "Антон", "Ахатовский", "ул. Гоголя 71А", "Фрунзенская", "89991234557",
         "22.10.2023", "трое суток", "серая безысходность", "коммент"]
    ])
    def test_order_scooter_general_flow(self, driver, button_order, name, surname, address, metro, phone, date, rent,
                                        color, comment):
        main = MainPage(driver)
        main.open()
        main.cookie_bar_closer()
        main.open_order_form(button_order)
        order = OrderPage(driver)
        order.fill_name(name)
        order.fill_surname(surname)
        order.fill_address(address)
        order.fill_metro(metro)
        order.fill_phone(phone)
        order.click_next_button()
        order.fill_date(date)
        order.fill_rent(rent)
        order.fill_color(color)
        order.fill_comment(comment)
        order.click_order_button()
        order.click_accept_order()

        assert 'Заказ оформлен' in order.get_order_status(), "Окно статуса не отобразилось"
