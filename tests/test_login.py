"""Start Page tests"""
from constants import login_constants
from pages.baseClass import BaseTest
from pages.login_page import LoginPage


class TestStartPage(BaseTest):
    """Test for start page"""

    def test_invalid_login(self):
        login_page_obj = LoginPage(self.driver)
        # enter invalid login
        login_page_obj.fill_login_fields(email="invalid@geniusee.com", password="12341234")
        self.logger.info("Invalid email and valid password are entered and LOGIN button is clicked")
        # get invalid email message
        login_page_obj.verify_invalid_email_error()
        self.logger.info("Invalid email error is displayed")

    def test_invalid_password(self):
        login_page_obj = LoginPage(self.driver)
        # enter invalid login
        login_page_obj.fill_login_fields(email="v.litvinenko+admin@geniusee.com", password="invalidpassword")
        self.logger.info("Valid email and invalid password are entered and LOGIN button is clicked")
        # get invalid message
        login_page_obj.verify_invalid_password_error()
        self.logger.info("Invalid password error is displayed")

    def test_valid_login(self):
        login_page_obj = LoginPage(self.driver)
        # enter valid login and password
        login_page_obj.fill_login_fields(email=login_constants.ADMIN_LOGIN, password=login_constants.ADMIN_PASSWORD)
        self.logger.info("Valid email and valid password are entered and LOGIN button is clicked")
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=login_constants.ADMIN_LOGIN.lower())
        self.logger.info("Valid email is logged in and verified")

    def test_forgot_password_is_opened(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.verify_forgot_password_page_is_opened()
        self.logger.info("Click the forgot button and verify the forgot page is opened")

    def test_error_message_invalid_email(self):
        login_page_obj = LoginPage(self.driver)
        # click forgot password link
        login_page_obj.verify_forgot_password_page_is_opened()
        # enter invalid mail into forgot mail field and click reset button
        login_page_obj.fill_forgot_section_fields(email="Invaid_email@gmail.com")
        # get error message
        login_page_obj.error_message_invalid_forgot_email()

    def test_valid_reset_of_user(self):
        login_page_obj = LoginPage(self.driver)
        # click forgot password link
        login_page_obj.verify_forgot_password_page_is_opened()
        # enter valid mail into forgot mail field and click RESET button
        login_page_obj.fill_forgot_section_fields(email=login_constants.TECHLAB_LOGIN)
        # get success message
        login_page_obj.verify_password_is_reset()

    def test_upper_case_login(self):
        login_page_obj = LoginPage(self.driver)
        # enter valid login and password
        login_page_obj.fill_login_fields(email=login_constants.ADMIN_LOGIN.upper(), password=login_constants.ADMIN_PASSWORD)
        self.logger.info("Valid email and valid password are entered and LOGIN button is clicked")
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=login_constants.ADMIN_LOGIN.lower())
        self.logger.info("Valid email is logged in and verified")
