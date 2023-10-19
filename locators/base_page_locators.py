from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопка Заказать вверху страницы
    UPPER_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"]
    # Кнопка Заказать внизу страницы
    BOTTOM_ORDER_BUTTON = [By.XPATH, "//div/p[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]"]

    # Блок "Вопросы о важном"
    # Сколько это стоит? И как оплатить?
    # PRICE_QUESTION = [By.XPATH, "//div[contains(text(), 'Сколько это стоит? И как оплатить?')]"]
    PRICE_QUESTION = [By.ID, "accordion__heading-0"]
    # Сутки — 400 рублей. Оплата курьеру — наличными или картой.
    PRICE_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру')]"]

    # Хочу сразу несколько самокатов! Так можно?
    # FEW_SCOOTER_QUESTION = [By.XPATH, "//div[contains(text(), 'Хочу сразу несколько самокатов!')]"]
    FEW_SCOOTER_QUESTION = [By.ID, "accordion__heading-1"]
    # Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями...
    FEW_SCOOTER_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Пока что у нас так: один заказ — один самокат.')]"]

    # Как рассчитывается время аренды?
    # RENT_TIME_QUESTION = [By.XPATH, "//div[contains(text(), 'Как рассчитывается время аренды?')]"]
    RENT_TIME_QUESTION = [By.ID, "accordion__heading-2"]
    # Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня...
    RENT_TIME_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая')]"]

    # Можно ли заказать самокат прямо на сегодня?
    # TODAY_ORDER_QUESTION = [By.XPATH, "//div[contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]"]
    TODAY_ORDER_QUESTION = [By.ID, "accordion__heading-3"]
    # Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    TODAY_ORDER_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Только начиная с завтрашнего дня.')]"]

    # Можно ли продлить заказ или вернуть самокат раньше?
    # DURATION_ORDER_QUESTION = [By.XPATH, "//div[contains(text(), 'Можно ли продлить заказ или вернуть самокат')]"]
    DURATION_ORDER_QUESTION = [By.ID, "accordion__heading-4"]
    # Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
    DURATION_ORDER_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Пока что нет! Но если что-то срочное — всегда можно позвонить')]"]

    # Вы привозите зарядку вместе с самокатом?
    # CHARGER_QUESTION = [By.XPATH, "//div[contains(text(), 'Вы привозите зарядку вместе с самокатом?')]"]
    CHARGER_QUESTION = [By.ID, "accordion__heading-5"]
    # Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — ...
    CHARGER_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Самокат приезжает к вам с полной зарядкой.')]"]

    # Можно ли отменить заказ?
    # CANCEL_QUESTION = [By.XPATH, "//div[contains(text(), 'Можно ли отменить заказ?')]"]
    CANCEL_QUESTION = [By.ID, "accordion__heading-6"]
    # Да, пока самокат не привезли. Штрафа не будет...
    CANCEL_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Да, пока самокат не привезли. Штрафа не будет')]"]

    # Я жизу за МКАДом, привезёте?
    # COUNTRYSIDE_QUESTION = [By.XPATH, "//div[contains(text(), 'Я жизу за МКАДом, привезёте?')]"]
    COUNTRYSIDE_QUESTION = [By.ID, "accordion__heading-7"]
    # Да, обязательно. Всем самокатов! И Москве, и Московской области.
    COUNTRYSIDE_ANSWER = [By.XPATH, "//div/p[contains(text(), 'Да, обязательно. Всем самокатов!')]"]