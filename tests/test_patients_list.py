import time
import random

import pytest
from selenium.webdriver.common.by import By

from constants.patient_list_constant import LIST_OF_PATIENTS_FIRSTMAMES_XPATH
from constants import login_constants, profile_constants, patient_list_constant, pages_menu_constant, \
    patient_profile_constant
from pages.login_page import LoginPage
from pages.patient_list_page import PatientsListPage
from pages.patient_profile_page import PatientProfilePage
from pages.profile_page import ProfilePage
from test_data.patients_data import PatientData
from test_data.users_data import UsersData


class TestPatients:
    """Here valid test data for patient creation"""
    @pytest.fixture(params=PatientData.VALID_PATIENT_CREATION_DATA)
    def get_patient_data(self, request):
        return request.param

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
        self.logger.info("Unique Patient is created")

        """enter valid patient first name into searchbox"""
        patient_list_obj.search_created_patient(get_patient_data['first_name'])
        self.logger.info("firstname of patient is entered into the searchbox")

        """Verify created patient is displayed into the patient list"""
        patient_list_obj.verify_patient_is_displayed_on_list(get_patient_data["first_name"])
        self.logger.info("firstname is validated after the patient is created")

    def test_count_of_patient_after_patient_creation_is_increased(self, get_patient_data, login_as_admin):
        """Go to the patient creation overlay"""
        patient_list_obj = PatientsListPage(self.driver)
        patient_list_obj.open_patient_overlay()
        self.logger.info("Patient overlay is clicked to be opened")

        """Get previous count of patients"""
        count_of_patients_before_patient_creation = patient_list_obj.count_of_patients()
        self.logger.info(f"Previous count of patients is displayed and = {count_of_patients_before_patient_creation}")

        """Create patient with valid email and unique first name"""
        patient_list_obj.create_valid_patient_with_unique_firstname(get_patient_data["first_name"],
                                                                    get_patient_data["last_name"],
                                                                    get_patient_data["email"],
                                                                    get_patient_data["phone"],
                                                                    patient_list_constant.PAYMENT_COEX_OPTION_XPATH)
        self.logger.info("Unique Patient is created")

        """Get current count of patients"""
        count_of_patients_after_patient_creation = patient_list_obj.count_of_patients()
        self.logger.info(f"Previous count of patients is displayed and = {count_of_patients_before_patient_creation}")

        """Verify count of patient is increased to 1"""
        assert count_of_patients_after_patient_creation == count_of_patients_before_patient_creation + 1
        self.logger.info(
            f"count of patient actual: {count_of_patients_before_patient_creation + 1} expected: {count_of_patients_after_patient_creation}")

    def test_verify_patient_is_removed_by_admin(self, get_patient_data, login_as_admin):
        """Go to the patient creation overlay"""
        patient_list_obj = PatientsListPage(self.driver)
        patient_profile_obj = PatientProfilePage(self.driver)
        patient_list_obj.open_patient_overlay()
        self.logger.info("Patient overlay is clicked to be opened")

        """Create patient with valid email and unique first name"""
        patient_list_obj.create_valid_patient_with_unique_firstname(get_patient_data["first_name"],
                                                                    get_patient_data["last_name"],
                                                                    get_patient_data["email"],
                                                                    get_patient_data["phone"],
                                                                    patient_list_constant.PAYMENT_COEX_OPTION_XPATH)

        """Get count of patients after patient creation"""
        count_after_patient_is_created = patient_list_obj.count_of_patients()
        self.logger.info(f"Patients count after the patient is created = {count_after_patient_is_created}")

        """open created patient"""
        patient_list_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        self.logger.info("Patient profile is opened")

        """click remove button to remove the patient"""
        patient_profile_obj.click_remove_button()
        self.logger.info("remove button is clicked")

        count_after_patient_is_removed = patient_list_obj.count_of_patients()
        self.logger.info(f"Patients count after the patient is removed = {count_after_patient_is_removed}")

        """Verify count of patients is decreased after the patient is removed"""
        assert count_after_patient_is_removed == count_after_patient_is_created-1

        """Input removed patient name into search"""
        patient_list_obj.search_created_patient(get_patient_data['first_name'])
        self.logger.info(f"firstname {get_patient_data['first_name']} of patient is entered into the searchbox")

        patient_list_obj.verify_removed_patient_is_not_displayed_on_list(get_patient_data['first_name'])
        self.logger.info("firstname of patient is not displayed")


