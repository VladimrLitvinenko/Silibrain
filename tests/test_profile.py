import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import login_constants, profile_constants
from pages import baseClass
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from test_data.users_data import UsersData


@pytest.mark.usefixtures("setup")
class TestUserProfilePage:
    """Test for user profile page"""

    def test_fields_are_edited(self, login_as_admin):
        """Login as admin"""
        profile_page_obj = ProfilePage(self.driver)

        """Click EDIT button in the profile"""
        profile_page_obj.click_edit_button()
        self.logger.info("Edit button is clicked")

        """Generate first name and last name"""
        first_name = baseClass.generate_random_text(1)
        last_name = baseClass.generate_random_text(1)

        """Input FIRST NAME, LAST NAME, PHONE"""
        profile_page_obj.input_text_into_fields(first_name=first_name, last_name=last_name, phone=UsersData.PHONE_INPUT)
        self.logger.info(
            f"first name= {first_name}  last name= {last_name}  phone= {UsersData.PHONE_INPUT} are entered")

        """Click SAVE button"""
        profile_page_obj.click_save_button()
        self.logger.info("SAVE button is clicked")

        profile_page_obj.verrify_the_fields_are_saved(first_name=first_name, last_name=last_name,
                                                      phone=UsersData.PHONE_INPUT)
        self.logger.info(
            f"first name= {first_name}  last name= {last_name}  phone= {UsersData.PHONE_INPUT}  are verified")

    def test_fields_are_disabled_by_default(self, setup , login_as_admin):
        profile_page_obj = ProfilePage(self.driver)
        profile_page_obj.verify_fields_are_disabled_by_default()
        self.logger.info("5 fields are read only by default")

