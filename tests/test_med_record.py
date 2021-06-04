import time

import pytest
from selenium.webdriver.common.by import By

from constants import patient_list_constant
from pages.med_record_page import MedRecordPage
from pages.patient_case_tab_page import CaseTabPage
from pages.patient_list_page import PatientsListPage
from test_data.patients_data import PatientData


@pytest.mark.usefixtures("setup")
class TestMedRecord:

    def test_placeholder_name(self, create_patient):
        med_record_obj = MedRecordPage(self.driver)
        med_record_obj.click_create_med_record_button()
        med_record_obj.verify_name_of_med_record_placeholder()