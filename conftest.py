import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    # driver.set_window_size(1200, 800)
    yield driver
    driver.quit()
