import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import login_constants
from pages.baseClass import AdminUser
from pages.login_page import LoginPage
from test_data.users_data import UsersData

@pytest.fixture(scope="class")
def login_as_admin():
    print("I will be executed first")
    yield
    print("I will be executed as last")


def pytest_runtest_setup(item):
    """prepare test"""
    log = logging.getLogger(item.name)
    item.cls.logger = log


def pytest_addoption(parser):
    """
    --browser_name  - ключ который мы пишем в команде перед наименованием браузера. Пример: py.test --browser_name firefox
    default="chrome" - означает что по умолчанию будет ранится хроме если мы не указали наименование браузера
    """
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="function")
def setup(request):
    """
    Теперь если мы можем запускать комманду с наимнованием нужного нам браузера для рана:
     py.test --browser_name firefox
     py.test --browser_name chrome
    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/home/ihor/PycharmProjects/Silibrain/driver/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/home/ihor/PycharmProjects/Silibrain/driver/geckodriver")
    # Open start page
    driver.get(login_constants.STAGE_BASE_URL)
    driver.implicitly_wait(time_to_wait=5)
    login_page_obj = LoginPage(driver)
    driver.maximize_window()
    # click ingressa button
    ingresa_button = driver.find_element(by=By.XPATH, value=login_constants.INGRESSA_BUTTON_LOGIN_PAGE)
    ingresa_button.click()

    """это означает что теперь наш драйвер может быть юзабельным на уровне класса"""
    request.cls.driver = driver

    yield login_page_obj
    driver.close()


@pytest.fixture(scope="function")
def login_as_admin(setup):
    admin_user_obj = AdminUser(email=UsersData.ADMIN_LOGIN, password=UsersData.ADMIN_PASSWORD)
    # enter valid login and password
    setup.fill_login_fields(email=UsersData.ADMIN_LOGIN, password=UsersData.ADMIN_PASSWORD)
    # Verify the email is displayed on the page
    setup.verify_success_login(email=UsersData.ADMIN_LOGIN.lower())
    return admin_user_obj