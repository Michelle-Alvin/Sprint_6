from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = [By.XPATH, "//input[@placeholder='* Имя']"]

    SURNAME_INPUT = [By.XPATH, "//input[@placeholder='* Фамилия']"]

    ADDRESS_INPUT = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    METRO_INPUT = [By.XPATH, "//input[@class='select-search__input']"]

    METRO_SELECT = [By.XPATH, "//div[@class='select-search__select']"]

    PHONE_INPUT = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]

    DATE_INPUT = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    RENT_TIME_INPUT = [By.XPATH, "//div[text()='* Срок аренды']"]

    BLACK_COLOR_CHECKBOX = [By.ID, "black"]

    GREY_COLOR_CHECKBOX = [By.ID, "grey"]

    COMMENT_INPUT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    ORDER_BUTTON = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"]

    ACCEPT_ORDER_BUTTON = [By.XPATH, "//button[text()='Да']"]

    ORDER_TITTLE = [By.XPATH, "//div[contains(class='Order_ModalHeader')]"]

    ORDER_STATUS = [By.XPATH, "//div[text()='Заказ оформлен']"]
