"""Start Page tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest


class TestStartPage(BaseTest):
    """Test for start page"""

    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Chrome(
            executable_path="/home/ihor/PycharmProjects/pythonQALightSelenium/drivers/chromedriver")
        driver.maximize_window()
        # Open start page
        driver.get("https://stg-hospitalprivadopeten.geniusee.space/")

        # click ingressa button
        ingresa_button = driver.find_element(by=By.XPATH, value="//span[text()='Ingresa']")
        ingresa_button.click()

        driver.implicitly_wait(time_to_wait=20)  # ждем пока найдет элемент
        yield driver
        driver.maximize_window()
        driver.close()

    def test_invalid_login(self, setup):
        driver = setup
        # enter invalid login
        email_input_field = driver.find_element(by=By.XPATH, value="//input[@name='email']")
        email_input_field.send_keys("v.litvinenko+admin3@geniusee.com")

        # enter valid password
        password_input_field = drддiver.find_element(by=By.XPATH, value="//input[@name='password']")
        password_input_field.send_keys("12341234")

        # Click on Sign in
        sign_in_button = driver.find_element(by=By.XPATH, value="//span[text()='Ingresa']")
        sign_in_button.click()

        # get invalid message
        email_error_message = driver.find_element(by=By.XPATH, value="//p[text()='Usuario no encontrado']")
        assert email_error_message.text == "Usuario no encontrado"

    def test_invalid_password(self, setup):
        driver = setup
        # enter valid login
        email_input_field = driver.find_element(by=By.XPATH, value="//input[@name='email']")
        email_input_field.send_keys("v.litvinenko+admin@geniusee.com")

        # enter invalid password
        password_input_field = driver.find_element(by=By.XPATH, value="//input[@name='password']")
        password_input_field.send_keys("1234123455")

        # Click on Sign in
        sign_in_button = driver.find_element(by=By.XPATH, value="//span[text()='Ingresa']")
        sign_in_button.click()

        # get invalid message
        password_error_message = driver.find_element(by=By.XPATH, value="//p[text()='Credenciales no validas']")
        assert password_error_message.text == "Credenciales no validas"

    def test_valid_login(self, setup):
        driver = setup
        # click ingressa button
        ingresa_button = driver.find_element(by=By.XPATH, value="//span[text()='Ingresa']")
        ingresa_button.click()

        # enter valid login
        email_input_field = driver.find_element(by=By.XPATH, value="//input[@name='email']")
        email_input_field.send_keys("v.litvinenko+admin@geniusee.com")

        # enter valid password
        password_input_field = driver.find_element(by=By.XPATH, value="//input[@name='password']")
        password_input_field.send_keys("12341234")
        # Click on Sign in
        sign_in_button = driver.find_element(by=By.XPATH, value="//span[text()='Ingresa']")
        sign_in_button.click()

        # Verify the error email is displayed on the page
        disabled_email_field = driver.find_element(by=By.XPATH,
                                                   value="//input[@value='v.litvinenko+admin@geniusee.com']")
        assert disabled_email_field.get_attribute('value') == "v.litvinenko+admin@geniusee.com"

    def test_forgot_password_is_opened(self, setup):
        driver = setup
        forgot_password_link = driver.find_element(by=By.XPATH, value="//a[@href='#/auth/forgot_password']")
        forgot_password_link.click()
        assert "forgot_password" in driver.current_url

    def test_error_message_invalid_email(self, setup):
        driver = setup

        # click forgot password link
        forgot_password_link = driver.find_element(by=By.XPATH, value="//a[@href='#/auth/forgot_password']")
        forgot_password_link.click()

        # enter invalid mail into forgot mail field
        forgot_email_field = driver.find_element(by=By.XPATH, value="//input[@name='email']")
        forgot_email_field.send_keys("invalid@gmail.com")

        # click reset button
        reset_button = driver.find_element(by=By.XPATH, value="//span[text()='Reajusta tu Cuenta']")
        reset_button.click()

        # get error message
        user_in_nof_found_message = driver.find_element(by=By.XPATH, value="//p[text()='Usuario no encontrado']")
        assert user_in_nof_found_message.text == "Usuario no encontrado"

    def test_valid_reset_of_user(self, setup):
        driver = setup

        # click forgot password link
        forgot_password_link = driver.find_element(by=By.XPATH, value="//a[@href='#/auth/forgot_password']")
        forgot_password_link.click()

        # enter valid mail into forgot mail field
        forgot_email_field = driver.find_element(by=By.XPATH, value="//input[@name='email']")
        forgot_email_field.send_keys("v.litvinenko+techlab@geniusee.com")

        # click reset button
        reset_button = driver.find_element(by=By.XPATH, value="//span[text()='Reajusta tu Cuenta']")
        reset_button.click()

        # get success message
        success_reset_message = driver.find_element(by=By.XPATH,
                                                    value="//p[contains(text(),'El enlace se envió a su correo electrónico permiti')]")
        assert success_reset_message.text == "El enlace se envió a su correo electrónico permitiendo configurar su contraseña"

    def test_print(self, setup):
        assert 1 == 1
