import time

import pytest
from selenium.webdriver.common.by import By

from constants import patient_list_constant
from pages.med_record_page import MedRecordPage
from pages.patient_case_tab import CaseTabPage
from pages.patient_list_page import PatientsListPage
from test_data.patients_data import PatientData


@pytest.mark.usefixtures("setup")
class TestMedRecord:
    @pytest.fixture(scope="function")
    def create_patient(self, login_as_admin, get_patient_data):
        patient_page_obj = PatientsListPage(self.driver)
        patient_page_obj.open_patient_list_page()
        patient_page_obj.open_patient_overlay()
        patient_page_obj.create_valid_patient_with_unique_firstname(get_patient_data["first_name"],
                                                                    get_patient_data["last_name"],
                                                                    get_patient_data["email"],
                                                                    get_patient_data["phone"],
                                                                    patient_list_constant.PAYMENT_COEX_OPTION_XPATH)
        patient_page_obj.open_created_patient_displayed_on_list(get_patient_data["first_name"])
        yield patient_page_obj

    def test_placeholder_name(self, create_patient):
        med_record_obj = MedRecordPage(self.driver)
        med_record_obj.click_create_med_record_button()
        med_record_obj.verify_name_of_med_record_placeholder()