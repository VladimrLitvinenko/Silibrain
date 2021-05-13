"""Start Page tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constants import login_constants
from pages.login_page import LoginPage


class TestStartPage(BaseTest):
    """Test for start page"""

    @pytest.fixture(scope="function")
    def setup(self):
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
        yield login_page_obj
        driver.close()

    def test_invalid_login(self, setup):
        login_page_obj = setup
        # enter invalid login
        login_page_obj.fill_login_fields(email="invalid@geniusee.com", password="12341234")
        self.logger.info("Invalid email and valid password are entered and LOGIN button is clicked")
        # get invalid email message
        login_page_obj.verify_invalid_email_error()
        self.logger.info("Invalid email error is displayed")

    def test_invalid_password(self, setup):
        login_page_obj = setup
        # enter invalid login
        login_page_obj.fill_login_fields(email="v.litvinenko+admin@geniusee.com", password="invalidpassword")
        self.logger.info("Valid email and invalid password are entered and LOGIN button is clicked")
        # get invalid message
        login_page_obj.verify_invalid_password_error()
        self.logger.info("Invalid password error is displayed")

    def test_valid_login(self, setup):
        login_page_obj = setup
        # enter valid login and password
        login_page_obj.fill_login_fields(email=login_constants.ADMIN_LOGIN, password=login_constants.ADMIN_PASSWORD)
        self.logger.info("Valid email and valid password are entered and LOGIN button is clicked")
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=login_constants.ADMIN_LOGIN.lower())
        self.logger.info("Valid email is logged in and verified")

    def test_forgot_password_is_opened(self, setup):
        login_page_obj = setup
        login_page_obj.verify_forgot_password_page_is_opened()
        self.logger.info("Click the forgot button and verify the forgot page is opened")

    def test_error_message_invalid_email(self, setup):
        login_page_obj = setup
        # click forgot password link
        login_page_obj.verify_forgot_password_page_is_opened()
        # enter invalid mail into forgot mail field and click reset button
        login_page_obj.fill_forgot_section_fields(email="Invaid_email@gmail.com")
        # get error message
        login_page_obj.error_message_invalid_forgot_email()

    def test_valid_reset_of_user(self, setup):
        login_page_obj = setup
        # click forgot password link
        login_page_obj.verify_forgot_password_page_is_opened()
        # enter valid mail into forgot mail field and click RESET button
        login_page_obj.fill_forgot_section_fields(email=login_constants.TECHLAB_LOGIN)
        # get success message
        login_page_obj.verify_password_is_reset()

    def test_upper_case_login(self, setup):
        login_page_obj = setup
        # enter valid login and password
        login_page_obj.fill_login_fields(email=login_constants.ADMIN_LOGIN.upper(), password=login_constants.ADMIN_PASSWORD)
        self.logger.info("Valid email and valid password are entered and LOGIN button is clicked")
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=login_constants.ADMIN_LOGIN.lower())
        self.logger.info("Valid email is logged in and verified")
