import logging
import random

import pytest
from selenium.webdriver.common.by import By

from constants import pages_menu_constant, patient_list_constant

"""Для всего класса теперь будет действовать setup fixture"""


class PatientsListPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open_patient_list_page(self):
        registros_patients_menu = self.driver.find_element(By.XPATH, value=pages_menu_constant.MENU_PATIENTS_XPATH)
        registros_patients_menu.click()

    def click_create_patient_button(self):
        ceate_patient_button = self.driver.find_element(By.XPATH, value=patient_list_constant.CREATE_PATIENT_BUTTON_XPATH)
        ceate_patient_button.click()

    def fill_unique_first_name_field(self, patient_first_name):
        first_name_field = self.driver.find_element(By.XPATH, value=patient_list_constant.FIRST_NAME_FIELD_XPATH)
        first_name_field.send_keys(patient_first_name)

    def fill_last_name_field(self):
        last_name_field = self.driver.find_element(By.XPATH, value=patient_list_constant.LAST_NAME_FIELD_XPATH)
        last_name_field.send_keys("TEST lastName 123")

    def input_valid_email_field(self, valid_patient_email):
        email_field = self.driver.find_element(By.XPATH, value=patient_list_constant.EMAIL_FIELD_XPATH)
        email_field.send_keys(valid_patient_email)

    def fill_phone_field(self):
        phone_field = self.driver.find_element(By.XPATH, value=patient_list_constant.PHONE_FIELD_XPATH)
        phone_field.send_keys("12341234")

    def select_payment_COEX_option(self):
        payment_field = self.driver.find_element(By.XPATH, value=patient_list_constant.PAYMENT_FIELD_XPATH)
        payment_field.click()
        payment_dropdown = self.driver.find_element(By.XPATH, value=patient_list_constant.PAYMENT_COEX_OPTION_XPATH)
        payment_dropdown.click()

    def click_create_on_patient_creation_overlay(self):
        create_client_button_on_popup = self.driver.find_element(By.XPATH, value=patient_list_constant.CREATE_PATIENT_BUTTON_ON_POP_UP_XPATH)
        create_client_button_on_popup.click()

    def verify_patient_is_created(self, patient_first_name):
        list_of_patients = self.driver.find_elements(By.XPATH, value=patient_list_constant.LIST_OF_PATIENTS_FIRSTMAMES)
        for each_patient in list_of_patients:
            if each_patient.text == patient_first_name:
                newly_added_patient = each_patient.text
                assert newly_added_patient == patient_first_name
                break

    def open_patient_overlay(self):
        """Go to the 'Registros de Pacientes' page"""
        self.open_patient_list_page()
        """Click 'create patient' button"""
        self.click_create_patient_button()

    def create_valid_patient_with_unique_firstname(self, unique_patient, valid_email):
        self.fill_unique_first_name_field(unique_patient)
        self.fill_last_name_field()
        self.input_valid_email_field(valid_email)
        self.fill_phone_field()
        self.select_payment_COEX_option()
        self.click_create_on_patient_creation_overlay()
