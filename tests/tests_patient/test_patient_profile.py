"""Opened tests_patient page"""
import time

import pytest
from selenium.webdriver.common.by import By

from constants import patient_profile_constant
from pages.baseClass import generate_random_text
from pages.patient_page.patient_case_tab_page import CaseTabPage
from pages.patient_page.patient_list_page import PatientsListPage
from pages.patient_page.patient_profile_page import PatientProfilePage
from test_data.patients_data import PatientData
from test_data.users_data import UsersData


@pytest.mark.usefixtures("setup")
class TestPatientProfile():
    """Here valid test data for tests_patient creation"""

    @pytest.fixture(params=PatientData.VALID_PATIENT_CREATION_DATA)
    def get_patient_data(self, request):
        return request.param

    def test_patient_status_is_null_by_default(self, create_patient, get_patient_data):
        patient_profile_list_obj = PatientsListPage(self.driver)
        patient_profile_obj = PatientProfilePage(self.driver)
        """
        - Open Patient profile page
        - Verify status is NULL by default
        """
        patient_profile_list_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        self.logger.info(f'Opened created patient is with the UNIQUE NAME = {get_patient_data["first_name"]}')
        patient_profile_obj.verify_patient_status(patient_profile_constant.PATIENT_NULL_STATUS)
        self.logger.info(f"Patient default status is {patient_profile_constant.PATIENT_NULL_STATUS}")

    def test_patient_status_is_changed_to_pendite_if_case_is_added(self, create_patient, get_patient_data):
        patient_profile_list_obj = PatientsListPage(self.driver)
        case_tab_page_obj = CaseTabPage(self.driver)
        patient_profile_page = PatientProfilePage(self.driver)
        """
        - Open created patient
        - Click CASE tab
        - Create case
        - Go to the patient profile page
        - Verify the status is PENDIENTE"""
        patient_profile_list_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        self.logger.info(f'Opened created patient is with the UNIQUE NAME = {get_patient_data["first_name"]}')
        case_tab_page_obj.click_case_tab()
        self.logger.info(f'Case tab is opened')
        case_tab_page_obj.create_case_with_default_date()
        self.logger.info(f'Case is created')
        patient_profile_page.click_profile_patient_tab()
        self.logger.info(f'Patient profile  is clicked')
        patient_profile_page.verify_patient_status(patient_profile_constant.PATIENT_PENDIENTE_STATUS)
        self.logger.info(f'{patient_profile_constant.PATIENT_PENDIENTE_STATUS} status is displayed ')

    def test_patient_status_is_changed_to_NULL_back_if_case_is_removed(self, create_patient, get_patient_data):
        patient_profile_list_obj = PatientsListPage(self.driver)
        case_tab_page_obj = CaseTabPage(self.driver)
        patient_profile_page = PatientProfilePage(self.driver)
        """
        - Open created patient
        - Click CASE tab
        - Create case
        - Remove case
        - Go to the patient profile page
        - Verify the status is NULL"""
        patient_profile_list_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        self.logger.info(f'Opened created patient is with the UNIQUE NAME = {get_patient_data["first_name"]}')
        case_tab_page_obj.click_case_tab()
        self.logger.info(f'Case tab is opened')
        case_tab_page_obj.create_case_with_default_date()
        self.logger.info(f'Case is created')
        case_tab_page_obj.open_newly_created_case()
        self.logger.info(f'newly created case is opened')
        case_tab_page_obj.click_remove_case_button()
        self.logger.info(f'case is removed')
        patient_profile_page.click_profile_patient_tab()
        self.logger.info(f'Patient profile  is clicked')
        patient_profile_page.verify_patient_status(patient_profile_constant.PATIENT_NULL_STATUS)
        self.logger.info(f'{patient_profile_constant.PATIENT_PENDIENTE_STATUS} status is displayed ')

    def test_patient_fields_are_updated(self, create_patient, get_patient_data):
        patient_profile_list_obj = PatientsListPage(self.driver)
        case_tab_page_obj = CaseTabPage(self.driver)
        patient_profile_page_obj = PatientProfilePage(self.driver)
        """
        - Open created patient
        - Click edit button
        - Update all fields
        - Click 'save' button
        - Update page
        - Verify the fields are updated
        """
        patient_name = generate_random_text(1)
        patient_last_name = generate_random_text(1)
        patient_email = generate_random_text(1)
        patient_phone_number = get_patient_data["phone"]

        patient_profile_list_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        self.logger.info(f'Opened created patient is with the UNIQUE NAME = {get_patient_data["first_name"]}')
        patient_profile_page_obj.click_edit_button()
        self.logger.info(f'Edit button is clicked')
        patient_profile_page_obj.fill_all_patient_fields(first_name=patient_name, last_name=patient_last_name, email=patient_email,
                                                         phone=patient_phone_number, budget=PatientData.CUENTA_PROPIA_BUDGET)
        self.logger.info(
            f'Patient name is entered into first name = {patient_name}, last name = {patient_last_name}, email = {patient_email}, phone = {patient_phone_number}, budget = {PatientData.CUENTA_PROPIA_BUDGET}')
        patient_profile_page_obj.click_save_button()
        self.logger.info("Save button is clicked")
        time.sleep(10)
        patient_profile_page_obj.verify_patient_name_is_updated(name=patient_name)
        patient_profile_page_obj.verify_patient_last_name_is_updated(last_name=patient_last_name)
        # patient_profile_page_obj.verify_patient_email_is_updated(email=patient_email)
        patient_profile_page_obj.verify_patient_phone_is_updated(phone=patient_phone_number)
        self.logger.info(
            f'Patient fields updated and name= {patient_name}, last name = {patient_last_name}, email = {patient_email}, phone = {patient_phone_number}, budget = {PatientData.CUENTA_PROPIA_BUDGET}')

    def test_assigning_medico(self, create_patient, get_patient_data):
        patient_profile_list_obj = PatientsListPage(self.driver)
        patient_profile_page_obj = PatientProfilePage(self.driver)
        """
        - Open created patient
        - Click edit button
        - Click Assign medico button
        - Select medico
        - Click assign button within assign overlay
        - Click 'save' button
        - Update page
        - Verify the medico is updated
        """
        patient_profile_list_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        self.logger.info(f'Opened created patient is with the UNIQUE NAME = {get_patient_data["first_name"]}')
        patient_profile_page_obj.click_edit_button()
        self.logger.info(f'Edit button is clicked')

        patient_profile_page_obj.click_assign_medico_button()
        self.logger.info("Medico assign button is clicked")
        patient_profile_page_obj.select_medico_within_dropdown_list(medico=UsersData.MEDICO_NAME_SURNAME)
        self.logger.info("Medico is selected within dropdown")
        patient_profile_page_obj.click_assign_button_within_assign_medico_overlay()
        self.logger.info("Assign button is clicked within assign medico overlay")
        patient_profile_page_obj.click_close_assign_overlay()
        self.logger.info("Close assign medico overlay is clicked")
        patient_profile_page_obj.click_save_button()
        self.logger.info("Save button is clicked")
        patient_profile_page_obj.verify_selected_medico_is_assigned(UsersData.MEDICO_NAME_SURNAME)
        self.logger.info(f"Medico is assigned and = {UsersData.MEDICO_NAME_SURNAME}")
        patient_profile_list_obj.open_patient_list_page()
        self.logger.info(f"Patient list page is opened")
        patient_profile_list_obj.verify_assigned_medico_is_displayed_on_list(patient_first_name = get_patient_data["first_name"],
                                                                             assigned_medico=UsersData.MEDICO_NAME_SURNAME)
        self.logger.info(f"Medico is assigned and = {UsersData.MEDICO_NAME_SURNAME} within patient list")


