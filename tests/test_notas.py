import time

import pytest
from selenium.webdriver.common.by import By

from constants import patient_list_constant
from pages.med_record_page import MedRecordPage
from pages.patient_case_tab_page import CaseTabPage
from pages.patient_list_page import PatientsListPage
from test_data.patients_data import PatientData


class TestNotas:
    @pytest.fixture(params=PatientData.VALID_PATIENT_CREATION_DATA)
    def get_patient_data(self, request):
        return request.param











        # list_of_days_within_opened_calendar = self.driver.find_elements(By.XPATH, value="//div[@role='presentation']/button/span/p")
        # for each_day in list_of_days_within_opened_calendar:
        #     if each_day.text == "24":
        #         each_day.click()
        # time.sleep(2)


        # create_case_button = self.driver.find_element(By.XPATH, value="//span[text()='Agregar nuevo caso']")
        # create_case_button.click()
        # time.sleep(2)

        # view_case_button = self.driver.find_element(By.XPATH, value="//span[text()='Agregar nuevo caso']")
        # create_case_button.click()








