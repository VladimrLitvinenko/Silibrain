import logging

import pytest
from selenium.webdriver.common.by import By

from constants import login_constants
from pages.baseClass import BasePage
from test_data.users_data import UsersData

"""Для всего класса теперь будет действовать setup fixture"""


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def fill_login_fields(self, email, password):
        # enter login
        email_input_field = self.driver.find_element(by=By.XPATH, value=login_constants.LOGIN_EMAIL_INPUT_FIELD)
        email_input_field.send_keys(email)
        # enter password
        password_input_field = self.driver.find_element(by=By.XPATH, value=login_constants.LOGIN_PASSWORD_INPUT_FIELD)
        password_input_field.send_keys(password)
        # click sign in button
        sign_in_button = self.driver.find_element(by=By.XPATH, value=login_constants.INGRESSA_BUTTON_LOGIN_PAGE)
        sign_in_button.click()
        self.logger.debug("SIGN IN button is clicked")

    def fill_valid_user_data(self, email, password):
        self.fill_login_fields(email=email, password=password)
        self.logger.debug(F"valid email {email} and password {password} are entered")

    def verify_invalid_email_error(self):
        email_error_message = self.driver.find_element(by=By.XPATH, value=login_constants.LOGIN_EMAIL_ERROR_MESSAGE)
        assert email_error_message.text == "Usuario no encontrado"
        self.logger.debug(F"invalid email is validated")

    def verify_invalid_password_error(self):
        password_error_message = self.driver.find_element(by=By.XPATH,
                                                          value=login_constants.LOGIN_PASSWORD_ERROR_MESSAGE)
        assert password_error_message.text == "Credenciales no validas"
        self.logger.debug("invalid password is validated")

    def verify_success_login(self, email):
        disabled_email_field = self.driver.find_element(by=By.XPATH, value=login_constants.AFTER_SUCCESS_LOGIN)
        assert disabled_email_field.get_attribute('value') == email
        self.logger.debug("user is logged in")

    def verify_forgot_password_page_is_opened(self):
        forgot_password_link = self.driver.find_element(by=By.XPATH, value=login_constants.LOGIN_FORGOT_PASSWORD_LINK)
        forgot_password_link.click()
        assert "forgot_password" in self.driver.current_url
        self.logger.debug("forgot password page is opened")

    def fill_forgot_section_fields(self, email):
        # enter invalid mail into forgot mail field
        forgot_email_field = self.driver.find_element(by=By.XPATH, value=login_constants.FORGOT_PAGE_EMAIL_INPUT_FIELD)
        forgot_email_field.send_keys(email)
        self.logger.debug("email is entered into the forgot field")

        # click reset button
        reset_button = self.driver.find_element(by=By.XPATH, value=login_constants.FORGOT_PAGE_REST_BUTTON)
        reset_button.click()
        self.logger.debug("reset button is clicked")

    def error_message_invalid_forgot_email(self):
        user_in_nof_found_message = self.driver.find_element(by=By.XPATH,
                                                             value=login_constants.FORGOT_PAGE_USER_NOT_FOUND_MESSAGE)
        assert user_in_nof_found_message.text == "Usuario no encontrado"
        self.logger.debug("error message is displayed")

    def verify_password_is_reset(self):
        success_reset_message = self.driver.find_element(by=By.XPATH,
                                                         value=login_constants.FORGOT_PAGE_SUCCESS_RESET_MESSAGE)
        assert success_reset_message.text == "El enlace se envió a su correo electrónico permitiendo configurar su contraseña"
        self.logger.debug("reset password message is displayed")

    def login_as_admin(self):
        self.fill_valid_user_data(email=UsersData.ADMIN_LOGIN, password=UsersData.ADMIN_PASSWORD)
        self.logger.debug("user is logged is as admin")
