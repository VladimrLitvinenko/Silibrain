import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import login_constants
from pages.login_page import LoginPage

def pytest_runtest_setup(item):
    """prepare test"""
    log = logging.getLogger(item.name)
    item.cls.logger = log


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome(
        executable_path="/home/ihor/PycharmProjects/pythonQALightSelenium/drivers/chromedriver")
    # Open start page
    driver.get(login_constants.STAGE_BASE_URL)
    driver.implicitly_wait(time_to_wait=20)
    login_page_obj = LoginPage(driver)
    driver.maximize_window()
    # click ingressa button
    ingresa_button = driver.find_element(by=By.XPATH, value=login_constants.INGRESSA_BUTTON_LOGIN_PAGE)
    ingresa_button.click()

    """это означает что теперь наш драйвер может быть юзабельным на уровне класса"""
    request.cls.driver = driver

    yield login_page_obj
    driver.close()
