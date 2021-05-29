"""Start Page tests"""
import pytest

from constants import login_constants
from pages.login_page import LoginPage
from test_data import users_data
from test_data.users_data import UsersData

@pytest.mark.usefixtures("setup")
class TestStartPage():
    """Test for start page"""

    @pytest.fixture(params=UsersData.INVALID_USER_RESTRICTIONS)
    def get_invalid_Data(self, request):
        return request.param

    def test_invalid_login(self, get_invalid_Data):
        login_page_obj = LoginPage(self.driver)
        # enter invalid login
        login_page_obj.fill_login_fields(email=get_invalid_Data["invalid_login"],
                                         password=get_invalid_Data["invalid_password"])
        self.logger.info("Invalid email and valid password are entered and LOGIN button is clicked")
        # get invalid email message
        login_page_obj.verify_invalid_email_error()
        self.logger.info("Invalid email error is displayed")

    def test_invalid_password(self, get_invalid_Data):
        login_page_obj = LoginPage(self.driver)
        # enter invalid login
        login_page_obj.fill_login_fields(email=UsersData.ADMIN_LOGIN, password=get_invalid_Data["invalid_password"])
        self.logger.info(F"Valid email {UsersData.ADMIN_LOGIN} and invalid password are entered and LOGIN "
                         F"button is clicked")
        # get invalid message
        login_page_obj.verify_invalid_password_error()
        self.logger.info("Invalid password error is displayed")

    def test_valid_login(self):
        login_page_obj = LoginPage(self.driver)
        # enter valid login and password
        login_page_obj.fill_login_fields(email=UsersData.ADMIN_LOGIN, password=UsersData.ADMIN_PASSWORD)
        self.logger.info("Valid email and valid password are entered and LOGIN button is clicked")
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=UsersData.ADMIN_LOGIN.lower())
        self.logger.info("Valid email is logged in and verified")

    def test_forgot_password_is_opened(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.verify_forgot_password_page_is_opened()
        self.logger.info("Click the forgot button and verify the forgot page is opened")

    def test_error_message_invalid_email(self, get_invalid_Data):
        login_page_obj = LoginPage(self.driver)
        # click forgot password link
        login_page_obj.verify_forgot_password_page_is_opened()
        self.logger.info("Click the forgot password link is clicked")
        # enter invalid mail into forgot mail field and click reset button
        login_page_obj.fill_forgot_section_fields(email=get_invalid_Data["invalid_login"])
        self.logger.info("fields are entered within forgot password section")
        # get error message
        login_page_obj.error_message_invalid_forgot_email()
        self.logger.info("Error message of invalid password is verified")

    def test_valid_reset_of_user(self):
        login_page_obj = LoginPage(self.driver)
        # click forgot password link
        login_page_obj.verify_forgot_password_page_is_opened()
        self.logger.info("Forgot password is opened")
        # enter valid mail into forgot mail field and click RESET button
        login_page_obj.fill_forgot_section_fields(email=UsersData.ADMIN_LOGIN)
        self.logger.info(f"Enter valid email into reset email field= {UsersData.ADMIN_LOGIN}")
        # get success message
        login_page_obj.verify_password_is_reset()
        self.logger.info(f"Reset Password text is verified")

    def test_upper_case_login(self):
        login_page_obj = LoginPage(self.driver)
        # enter valid login and password
        login_page_obj.fill_login_fields(email=UsersData.ADMIN_LOGIN.upper(),
                                         password=UsersData.ADMIN_PASSWORD)
        self.logger.info("Valid email and valid password are entered and LOGIN button is clicked")
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=UsersData.ADMIN_LOGIN.lower())
        self.logger.info("Valid email is logged in and verified")
