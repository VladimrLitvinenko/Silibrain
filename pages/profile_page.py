import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import login_constants, profile_constants
from pages.baseClass import  BasePage
from pages.login_page import LoginPage

"""Для всего класса теперь будет действовать setup fixture"""


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def verify_all_fields_are_disabled_by_default(self):
        firstName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD_XPATH)
        lastName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_LAST_NAME_FIELD_XPATH)
        phone_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_PHONE_NUMBER_FIELD_XPATH)
        assert firstName_field.get_attribute("disabled")
        assert lastName_field.get_attribute("disabled")
        assert phone_field.get_attribute("disabled")

    def click_edit_button(self):
        edit_button = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_EDIT_BUTTON)
        edit_button.click()

    def input_text_into_fields(self, first_name, last_name, phone):
        """Highlight and the BACKSPACE text into first_name, last_name, phone """
        self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD_XPATH).send_keys(Keys.CONTROL+"A",Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_LAST_NAME_FIELD_XPATH).send_keys(Keys.CONTROL+"A",Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_PHONE_NUMBER_FIELD_XPATH).send_keys(Keys.CONTROL+"A",Keys.BACKSPACE)

        """Intupt text into first_name, last_name, phone """
        firstName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD_XPATH)
        lastName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_LAST_NAME_FIELD_XPATH)
        phone_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_PHONE_NUMBER_FIELD_XPATH)

        firstName_field.send_keys(first_name)
        lastName_field.send_keys(last_name)
        phone_field.send_keys(phone)

    def click_save_button(self, first_name, last_name, phone):
        """Click save button and refresh the page"""
        click_button = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_SAVE_BUTTON)
        click_button.click()
        self.driver.refresh()
        time.sleep(4)

        new_first_name = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD_XPATH).get_attribute('value')
        new_last_name = self.driver.find_element(By.XPATH, value= profile_constants.PROFILE_LAST_NAME_FIELD_XPATH).get_attribute('value')
        new_phone  = self.driver.find_element(By.XPATH, value= profile_constants.PROFILE_PHONE_NUMBER_FIELD_XPATH).get_attribute('value')
        assert first_name == new_first_name
        assert last_name == new_last_name
        assert phone == new_phone
        self.logger.debug(F"{first_name} field is equal to inputted {new_phone}")
        self.logger.debug(F"{last_name} field is equal to inputted {new_last_name}")
        self.logger.debug(F"{phone} field is equal to inputted {new_phone}")




















