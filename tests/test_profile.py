import logging
import time

from selenium.webdriver.common.by import By
from pages.baseClass import BaseTest
from constants import login_constants, profile_constants
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestUserProfilePage(BaseTest):
    """Test for user profile page"""


    def test_all_fields_are_disabled_by_default(self):
        """
        - Login as admin
        - verify the First name is disabled initially
        """
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_as_admin()
        profile_page_obj = ProfilePage(self.driver)
        profile_page_obj.verify_all_fields_are_disabled_by_default()

    def test_fields_are_edited(self):
        """Login as admin"""
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_as_admin()

        """Click EDIT button in the profile"""
        profile_page_obj = ProfilePage(self.driver)
        profile_page_obj.click_edit_button()

        """Clear all editable fields"""
        time.sleep(2)
        self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_FIRST_NAME_FIELD).clear()
        self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_LAST_NAME_FIELD).clear()
        self.driver.find_element(By.XPATH, value=profile_constants.PROFILE_PHONE_NUMBER_FIELD).clear()

        """Input FIRST NAME, LAST NAME, PHONE"""
        profile_page_obj.input_text_into_fields(first_name=profile_constants.FIRST_NAME_INPUT, last_name=profile_constants.LAST_NAME_INPUT, phone=profile_constants.PHONE_INPUT)
        profile_page_obj.click_save_button()
        #
        # print(self.driver.find_element(By.XPATH, value=profile_constants.FIRST_NAME_INPUT).get_attribute("value"), "GGGG", profile_constants.FIRST_NAME_INPUT)
        # assert self.driver.find_element(By.XPATH, value=profile_constants.FIRST_NAME_INPUT).get_attribute("value") == profile_constants.FIRST_NAME_INPUT




    # def test_all_fields_are_not_required(self):
    #     """
    #     - clear all fields
    #     - click save button
    #     """
    #     pass
