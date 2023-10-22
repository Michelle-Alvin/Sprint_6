from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка Заказать вверху страницы
    UPPER_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"]
    # Кнопка Заказать внизу страницы
    BOTTOM_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]"]

    # Блок "Вопросы о важном"
    # Сколько это стоит? И как оплатить?
    PRICE_QUESTION = [By.ID, "accordion__heading-0"]
    # Сутки — 400 рублей. Оплата курьеру — наличными или картой.
    PRICE_ANSWER = [By.ID, "accordion__panel-0"]

    # Хочу сразу несколько самокатов! Так можно?
    FEW_SCOOTER_QUESTION = [By.ID, "accordion__heading-1"]
    # Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями...
    FEW_SCOOTER_ANSWER = [By.ID, "accordion__panel-1"]

    # Как рассчитывается время аренды?
    RENT_TIME_QUESTION = [By.ID, "accordion__heading-2"]
    # Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня...
    RENT_TIME_ANSWER = [By.ID, "accordion__panel-2"]

    # Можно ли заказать самокат прямо на сегодня?
    TODAY_ORDER_QUESTION = [By.ID, "accordion__heading-3"]
    # Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    TODAY_ORDER_ANSWER = [By.ID, "accordion__panel-3"]

    # Можно ли продлить заказ или вернуть самокат раньше?
    DURATION_ORDER_QUESTION = [By.ID, "accordion__heading-4"]
    # Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
    DURATION_ORDER_ANSWER = [By.ID, "accordion__panel-4"]

    # Вы привозите зарядку вместе с самокатом?
    CHARGER_QUESTION = [By.ID, "accordion__heading-5"]
    # Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — ...
    CHARGER_ANSWER = [By.ID, "accordion__panel-5"]

    # Можно ли отменить заказ?
    CANCEL_QUESTION = [By.ID, "accordion__heading-6"]
    # Да, пока самокат не привезли. Штрафа не будет...
    CANCEL_ANSWER = [By.ID, "accordion__panel-6"]

    # Я жизу за МКАДом, привезёте?
    COUNTRYSIDE_QUESTION = [By.ID, "accordion__heading-7"]
    # Да, обязательно. Всем самокатов! И Москве, и Московской области.
    COUNTRYSIDE_ANSWER = [By.ID, "accordion__panel-7"]
