import time
import random

from selenium.webdriver.common.by import By
from pages.baseClass import BaseTest
from constants import login_constants, profile_constants, patient_list_constant, pages_menu_constant
from pages.login_page import LoginPage
from pages.patient_list_page import PatientsListPage
from pages.profile_page import ProfilePage


class TestPatients(BaseTest):

    def test_patient_is_created(self):
        """login as admin"""
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_as_admin()

        """Go to the 'Registros de Pacientes' page"""
        patient_list_obj = PatientsListPage(self.driver)
        patient_list_obj.open_patient_overlay()

        """Create patient with valid email and unique first name"""
        patient_list_obj.create_valid_patient_with_unique_firstname(unique_patient=patient_list_constant.UNIQUE_PATIENT_FIRSTNAME, valid_email=patient_list_constant.VALID_PATIENT_EMAIL)

        """Verify created patient is displayed into the patient list"""
        patient_list_obj.verify_patient_is_created(patient_list_constant.UNIQUE_PATIENT_FIRSTNAME)



