import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    # driver.set_window_size(1200, 800)
    yield driver
    driver.quit()