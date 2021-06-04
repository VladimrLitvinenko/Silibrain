import logging
import random
import time

import pytest
from selenium.webdriver.common.by import By

from constants import pages_menu_constant, patient_list_constant
from pages.baseClass import BasePage

"""Для всего класса теперь будет действовать setup fixture"""


class PatientsListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def open_patient_list_page(self):
        self.wait_until_click(locator_type=By.XPATH, locator= pages_menu_constant.MENU_PATIENTS_XPATH)
        self.logger.debug("patient list is opened")

    def click_create_patient_button(self):
        ceate_patient_button = self.driver.find_element(By.XPATH, value=patient_list_constant.CREATE_PATIENT_BUTTON_XPATH)
        ceate_patient_button.click()
        self.logger.debug("create patient button is clicked")

    def fill_unique_first_name_field(self, patient_first_name):
        self.wait_until_send_keys(By.XPATH, patient_list_constant.FIRST_NAME_FIELD_XPATH, patient_first_name)
        self.logger.debug(f"unique patient name is entered as {patient_first_name}")

    def fill_last_name_field(self, last_name):
        self.wait_until_send_keys(locator_type=By.XPATH, locator=patient_list_constant.LAST_NAME_FIELD_XPATH, data=last_name)
        self.logger.debug(f"unique patient last name is entered as {last_name}")

    def input_valid_email_field(self, valid_patient_email):
        self.wait_until_send_keys(locator_type=By.XPATH, locator=patient_list_constant.EMAIL_FIELD_XPATH, data=valid_patient_email)
        self.logger.debug(f"unique patient email is entered as {valid_patient_email}")

    def fill_phone_field(self, phone):
        self.wait_until_send_keys(locator_type=By.XPATH, locator=patient_list_constant.PHONE_FIELD_XPATH, data=phone)
        self.logger.debug(f"unique patient phone is entered = {phone}")


    def select_payment_option(self, payment_option):

        payment_field = self.driver.find_element(By.XPATH, value=patient_list_constant.PAYMENT_FIELD_XPATH)
        payment_field.click()
        payment_dropdown = self.driver.find_element(By.XPATH, value=payment_option)
        payment_dropdown.click()
        self.logger.debug("payment option is selected into the patient creation overlay")


    def click_create_on_patient_creation_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator=patient_list_constant.CREATE_PATIENT_BUTTON_ON_POP_UP_XPATH)
        self.logger.debug("create patient button is clicked on the creation overlay")

    def verify_patient_is_displayed_on_list(self, patient_first_name):
        list_of_patients = self.driver.find_elements(By.XPATH, value=patient_list_constant.LIST_OF_PATIENTS_FIRSTMAMES_XPATH)
        for each_patient in list_of_patients:
            if each_patient.text == patient_first_name:
                self.logger.debug(f"expected {patient_first_name} actual result {each_patient.text}")
                assert patient_first_name == each_patient.text


    def open_patient_overlay(self):
        """Go to the 'Registros de Pacientes' page"""
        self.open_patient_list_page()
        """Click 'create patient' button"""
        self.click_create_patient_button()

    def create_valid_patient_with_unique_firstname(self, first_name, last_name, email, phone, payment_option):
        self.fill_unique_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.input_valid_email_field(email)
        self.fill_phone_field(phone)
        self.select_payment_option(payment_option)
        self.click_create_on_patient_creation_overlay()
        time.sleep(6)

    def search_created_patient(self, first_name):
        self.wait_until_find(locator_type=By.XPATH, locator=patient_list_constant.SEARCH_TEXTBOX)
        self.wait_until_send_keys(locator_type=By.XPATH, locator=patient_list_constant.SEARCH_TEXTBOX, data=first_name)
        # get_search_box = self.wait_until_find(By.XPATH, patient_list_constant.SEARCH_TEXTBOX)
        # get_search_box.send_keys(first_name)
        self.logger.debug(f"{first_name} of patient is entered into the searchbox")
        time.sleep(1)

    def count_of_patients(self):
        time.sleep(2)
        pagination_element = self.driver.find_element(By.XPATH, value="//div[@class='MuiTablePagination-root']/div/p[2]").text
        self.logger.debug(f"pagination element shows the following info = {pagination_element} and split = {pagination_element.split()}")
        count_of_patients = pagination_element.split()
        self.logger.debug(f"count of patients = {count_of_patients[2]}")
        return int(count_of_patients[2])

    def open_created_patient_displayed_on_list(self, patient_first_name):
        list_of_patients = self.driver.find_elements(By.XPATH, value=patient_list_constant.LIST_OF_PATIENTS_FIRSTMAMES_XPATH)
        for each_patient in list_of_patients:
            if each_patient.text == patient_first_name:
                each_patient.click()
                self.logger.debug(f"created patient is opened")
                break

    def verify_removed_patient_is_not_displayed_on_list(self, patient_first_name):
        list_of_patients = self.driver.find_elements(By.XPATH, value=patient_list_constant.LIST_OF_PATIENTS_FIRSTMAMES_XPATH)
        for each_patient in list_of_patients:
            if each_patient.text != patient_first_name:
                self.logger.debug(f" {patient_first_name} is removed")
                assert patient_first_name == ""





