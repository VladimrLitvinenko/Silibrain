import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import login_constants, profile_constants
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from test_data.users_data import UsersData


class TestUserProfilePage:
    """Test for user profile page"""



    def test_fields_are_edited(self):
        """Login as admin"""
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_as_admin()

        """Click EDIT button in the profile"""
        profile_page_obj = ProfilePage(self.driver)    # def test_all_fields_are_disabled_by_default(self):
        """
        - Login as admin
        - verify the First name is disabled initially
        """
        profile_page_obj.click_edit_button()

        """Input FIRST NAME, LAST NAME, PHONE"""
        profile_page_obj.input_text_into_fields(first_name=UsersData.FIRST_NAME_INPUT,last_name=UsersData.LAST_NAME_INPUT, phone=UsersData.PHONE_INPUT)
        profile_page_obj.click_save_button(first_name=UsersData.FIRST_NAME_INPUT, last_name=UsersData.LAST_NAME_INPUT,  phone=UsersData.PHONE_INPUT)

        #
        # print(self.driver.find_element(By.XPATH, value=profile_constants.FIRST_NAME_INPUT).get_attribute("value"), "GGGG", profile_constants.FIRST_NAME_INPUT)
        # assert self.driver.find_element(By.XPATH, value=profile_constants.FIRST_NAME_INPUT).get_attribute("value") == profile_constants.FIRST_NAME_INPUT

    # def test_all_fields_are_not_required(self):
    #     """
    #     - clear all fields
    #     - click save button
    #     """
    #     pass
