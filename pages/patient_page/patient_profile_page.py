import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import patient_profile_constant
from pages.baseClass import BasePage


class PatientProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def click_remove_button(self):
        remove_patient_button = self.driver.find_element(By.XPATH, value=patient_profile_constant.REMOVE_PATIENT_XPATH)
        remove_patient_button.click()

    def click_edit_button(self):
        edit_patient_button = self.driver.find_element(By.XPATH,
                                                       value=patient_profile_constant.EDIT_BUTTON_PATIENT_XPATH)
        edit_patient_button.click()

    def verify_patient_status(self, patient_status):
        status = self.wait_for_text(locator_type=By.XPATH,
                                    locator=patient_profile_constant.PATIENT_PROFILE_STATUS_XPATH, text=patient_status)
        displayed_status_text = self.driver.find_element(By.XPATH,
                                                         patient_profile_constant.PATIENT_PROFILE_STATUS_XPATH).text
        splited_status_text = displayed_status_text.split()
        self.logger.debug(f"Paptient status is matched to {patient_status} == {splited_status_text[3]}")
        assert splited_status_text[3] == patient_status

    def click_profile_patient_tab(self):
        profile_tab = self.driver.find_element(By.XPATH, value=patient_profile_constant.PATIENT_PROFILE_TAB_XPATH)
        profile_tab.click()

    def fill_unique_first_name_field(self, first_name):
        """Clear the fields"""
        first_name_field = self.driver.find_element(By.XPATH,
                                                    value=patient_profile_constant.PATIENT_FIRST_NAME_FIELD_XPATH)
        first_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        first_name_field.send_keys(first_name)

    def fill_unique_last_name_field(self, last_name):
        """Clear the fields"""
        last_name_field = self.driver.find_element(By.XPATH,
                                                   value=patient_profile_constant.PATIENT_LAST_NAME_FIELD_XPATH)
        last_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        last_name_field.send_keys(last_name)

    def fill_unique_email_field(self, email):
        """Clear the fields"""
        last_name_field = self.driver.find_element(By.XPATH,
                                                   value=patient_profile_constant.PATIENT_EMAIL_FIELD_XPATH)
        last_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        last_name_field.send_keys(f"{email}@gmail.com")

    def fill_phone_number_field(self, phone):
        """Clear the fields"""
        last_phone_field = self.driver.find_element(By.XPATH,
                                                    value=patient_profile_constant.PATIENT_PHONE_FIELD_XPATH)
        last_phone_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        last_phone_field.send_keys(phone)

    def select_budget_type_within_dropdown(self, budget):
        click_to_expand_dropdown = self.driver.find_element(By.XPATH,
                                                            value=patient_profile_constant.BUDGET_DROPDOWN_ELEMENTS)
        click_to_expand_dropdown.click()
        budget_elements_list = self.driver.find_elements(By.XPATH,
                                                         value=patient_profile_constant.BUDGET_DROPDOWN_ELEMENT)
        for each_budget in budget_elements_list:
            if each_budget.text == budget:
                each_budget.click()

    def click_assign_medico_button(self):
        self.wait_until_click(locator_type=By.XPATH, locator=patient_profile_constant.ASIGNARLE_MEDICO)

    def select_medico_within_dropdown_list(self, medico):
        self.wait_until_click(locator_type=By.XPATH, locator="//div[@aria-labelledby='mui-component-select-doctor']")

        list_of_medicos = self.driver.find_elements(By.XPATH, value="//ul[@role='listbox']/li")
        for each_medico in list_of_medicos:
            if each_medico.text == medico:
                each_medico.click()

    def click_assign_button_within_assign_medico_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator="//span[text()='Asignar']")

    def click_close_assign_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator="//span[text()='Cerrar']")

    def click_save_button(self):
        edit_patient_button = self.driver.find_element(By.XPATH,
                                                       value=patient_profile_constant.EDIT_BUTTON_PATIENT_XPATH)
        edit_patient_button.click()


