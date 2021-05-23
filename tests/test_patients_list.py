import time
import random

import pytest
from selenium.webdriver.common.by import By
from pages.baseClass import BaseTest, AdminUser
from constants import login_constants, profile_constants, patient_list_constant, pages_menu_constant
from pages.login_page import LoginPage
from pages.patient_list_page import PatientsListPage
from pages.profile_page import ProfilePage
from test_data.patients_data import PatientData
from test_data.users_data import UsersData


class TestPatients(BaseTest):
    """Here valid test data for patient creation"""

    @pytest.fixture(params=PatientData.VALID_PATIENT_CREATION_DATA)
    def get_patient_data(self, request):
        return request.param

    @pytest.fixture(scope="function")
    def login_as_admin(self):
        login_page_obj = LoginPage(self.driver)
        # call User class with user data
        admin_user_obj = AdminUser(email=UsersData.ADMIN_LOGIN, password=UsersData.ADMIN_PASSWORD)
        # enter valid login and password
        login_page_obj.fill_login_fields(email=UsersData.ADMIN_LOGIN, password=UsersData.ADMIN_PASSWORD)
        # Verify the email is displayed on the page
        login_page_obj.verify_success_login(email=UsersData.ADMIN_LOGIN.lower())
        return admin_user_obj

    def test_patient_is_searchable(self, get_patient_data, login_as_admin):
        """Go to the patient creation overlay"""
        patient_list_obj = PatientsListPage(self.driver)
        patient_list_obj.open_patient_overlay()
        self.logger.info("patient creation overlay is opened")

        """Create patient with valid email and unique first name"""
        patient_list_obj.create_valid_patient_with_unique_firstname(get_patient_data["first_name"],
                                                                    get_patient_data["last_name"],
                                                                    get_patient_data["email"],
                                                                    get_patient_data["phone"],
                                                                    patient_list_constant.PAYMENT_COEX_OPTION_XPATH)
        """enter valid patient first name into searchbox"""
        patient_list_obj.search_created_patient(get_patient_data['first_name'])
        self.logger.info("firstname of patient is entered into the searchbox")

        """Verify created patient is displayed into the patient list"""
        patient_list_obj.verify_patient_is_displayed_on_list(get_patient_data["first_name"])
        self.logger.info("firstname is validated after the patient is created")
