from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure


class TestHeaderBar:
    @allure.title(f'Проверка клика по лого "Самокат"')
    def test_scooter_logo_return_to_main_page(self, driver):
        main = MainPage(driver)
        main.open()
        main.cookie_bar_closer()
        main.open_order_form()
        assert "https://qa-scooter.praktikum-services.ru/order" == driver.current_url, "Не выполнен переход на форму заказа"
        order = OrderPage(driver)
        order.go_to_main()

        assert "https://qa-scooter.praktikum-services.ru/" == driver.current_url, "Не выполнен переход на главную страницу"

    @allure.title(f'Проверка клика по лого "Яндекс"')
    def test_yandex_logo_redirect(self, driver):
        main = MainPage(driver)
        main.open()
        main.go_to_dzen()
        assert "https://dzen.ru/?yredirect=true" == driver.current_url
