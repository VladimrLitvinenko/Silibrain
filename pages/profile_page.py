import logging
import time

import pytest
from selenium.webdriver.common.by import By

from constants import login_constants, profile_constants
from pages.baseClass import BaseTest
from pages.login_page import LoginPage

"""Для всего класса теперь будет действовать setup fixture"""


class ProfilePage(BaseTest):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def verify_all_fields_are_disabled_by_default(self):
        firstName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD)
        lastName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_LAST_NAME_FIELD)
        phone_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_PHONE_NUMBER_FIELD)
        assert firstName_field.get_attribute("disabled")
        assert lastName_field.get_attribute("disabled")
        assert phone_field.get_attribute("disabled")

    def click_edit_button(self):
        edit_button = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_EDIT_BUTTON)
        edit_button.click()

    def click_save_button(self):
        click_button = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_SAVE_BUTTON)
        click_button.click()

    def input_text_into_fields(self, first_name, last_name, phone):
        firstName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD)
        lastName_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_LAST_NAME_FIELD)
        phone_field = self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_PHONE_NUMBER_FIELD)
        time.sleep(1)

        firstName_field.send_keys(first_name)
        lastName_field.send_keys(last_name)
        phone_field.send_keys(phone)














