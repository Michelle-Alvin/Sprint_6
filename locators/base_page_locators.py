from selenium.webdriver.common.by import By

class BasePageLocators:
    COOKIE_BANNER = [By.ID, "rcc-confirm-button"]

    SCOOTER_LOGO = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"]

    YANDEX_LOGO = [By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"]
