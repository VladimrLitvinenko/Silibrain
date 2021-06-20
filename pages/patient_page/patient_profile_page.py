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
        self.logger.debug(f"Remove button is clicked")

    def click_edit_button(self):
        edit_patient_button = self.driver.find_element(By.XPATH,
                                                       value=patient_profile_constant.EDIT_BUTTON_PATIENT_XPATH)
        edit_patient_button.click()
        self.logger.debug(f"Edit button is clicked")

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
        self.logger.debug(f"Patient profile tab is clicked")

    def fill_unique_first_name_field(self, first_name):
        """Clear the fields"""
        first_name_field = self.driver.find_element(By.XPATH,
                                                    value=patient_profile_constant.PATIENT_FIRST_NAME_FIELD_XPATH)
        first_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        first_name_field.send_keys(first_name)
        self.logger.debug(f"First name field is cleared and entered as = {first_name}")

    def fill_unique_last_name_field(self, last_name):
        """Clear the fields"""
        last_name_field = self.driver.find_element(By.XPATH,
                                                   value=patient_profile_constant.PATIENT_LAST_NAME_FIELD_XPATH)
        last_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        last_name_field.send_keys(last_name)
        self.logger.debug(f"Last name field is cleared and entered as = {last_name}")

    def fill_unique_email_field(self, email):
        """Clear the fields"""
        last_name_field = self.driver.find_element(By.XPATH,
                                                   value=patient_profile_constant.PATIENT_EMAIL_FIELD_XPATH)
        last_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        last_name_field.send_keys(f"{email}@gmail.com")
        self.logger.debug(f"Email field is cleared and entered as = {email}@gmail.com")

    def fill_phone_number_field(self, phone):
        """Clear the fields"""
        last_phone_field = self.driver.find_element(By.XPATH,
                                                    value=patient_profile_constant.PATIENT_PHONE_FIELD_XPATH)
        last_phone_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        """Input data into the fields"""
        last_phone_field.send_keys(phone)
        self.logger.debug(f"Phone field is cleared and entered as = {phone}")

    def select_budget_type_within_dropdown(self, budget):
        click_to_expand_dropdown = self.driver.find_element(By.XPATH,
                                                            value=patient_profile_constant.BUDGET_DROPDOWN_ELEMENTS)
        click_to_expand_dropdown.click()
        budget_elements_list = self.driver.find_elements(By.XPATH,
                                                         value=patient_profile_constant.BUDGET_DROPDOWN_ELEMENT)
        for each_budget in budget_elements_list:
            if each_budget.text == budget:
                each_budget.click()
        self.logger.debug(f"Budget is selected as = {patient_profile_constant.BUDGET_DROPDOWN_ELEMENT}")

    def fill_all_patient_fields(self, first_name, last_name, email, phone, budget):
        self.fill_unique_first_name_field(first_name)
        self.fill_unique_last_name_field(last_name)
        self.fill_unique_email_field(email)
        self.fill_phone_number_field(phone)
        self.select_budget_type_within_dropdown(budget)

    def click_assign_medico_button(self):
        self.wait_until_click(locator_type=By.XPATH, locator=patient_profile_constant.ASIGNARLE_MEDICO)
        self.logger.debug(f"Assign medico button is clicked")

    def select_medico_within_dropdown_list(self, medico):
        self.wait_until_click(locator_type=By.XPATH, locator="//div[@aria-labelledby='mui-component-select-doctor']")

        list_of_medicos = self.driver.find_elements(By.XPATH, value="//ul[@role='listbox']/li")
        for each_medico in list_of_medicos:
            if each_medico.text == medico:
                each_medico.click()
                self.logger.debug(f"Medico is selected within dropdown and = {medico}")

    def click_assign_button_within_assign_medico_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator="//span[text()='Asignar']")
        self.logger.debug(f"Assign button is clicked within assign overlay")

    def click_close_assign_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator="//span[text()='Cerrar']")
        self.logger.debug(f"Close button is clicked within assign overlay")

    def click_save_button(self):
        edit_patient_button = self.driver.find_element(By.XPATH,
                                                       value=patient_profile_constant.EDIT_BUTTON_PATIENT_XPATH)
        edit_patient_button.click()
        self.driver.refresh()
        self.logger.debug(f"Save button is clicked and browser is refreshed")

    def verify_patient_name_is_updated(self, name):
        assert self.wait_until_find(By.XPATH, patient_profile_constant.PATIENT_FIRST_NAME_FIELD_XPATH).get_attribute('value') == name
        self.logger.debug(f"Patient name is updated = {name}")

    def verify_patient_last_name_is_updated(self, last_name):
        assert self.wait_until_find(By.XPATH, patient_profile_constant.PATIENT_LAST_NAME_FIELD_XPATH).get_attribute('value') == last_name
        self.logger.debug(f"Patient last name is updated = {last_name}")

    def verify_patient_email_is_updated(self, email):
        assert self.wait_until_find(By.XPATH, patient_profile_constant.PATIENT_EMAIL_FIELD_XPATH).get_attribute('value') == email
        self.logger.debug(f"Patient email is updated = {email}")

    def verify_patient_phone_is_updated(self, phone):
        assert self.wait_until_find(By.XPATH, patient_profile_constant.PATIENT_PHONE_FIELD_XPATH).get_attribute('value') == phone
        self.logger.debug(f"Patient phone is updated = {phone}")

    def verify_patient_budget_is_updated(self, budget):
        assert self.wait_until_find(By.XPATH, patient_profile_constant.BUDGET_DROPDOWN_ELEMENT).get_attribute('value') == budget
        self.logger.debug(f"Patient budget is updated = {budget}")

    def verify_all_patient_fields_update(self, name, last_name, email, phone, budget):
        assert self.verify_patient_name_is_updated(name)
        assert self.verify_patient_last_name_is_updated(last_name)
        assert self.verify_patient_email_is_updated(email)
        assert self.verify_patient_phone_is_updated(phone)
        assert self.verify_patient_budget_is_updated(budget)

    def verify_selected_medico_is_assigned(self, assigned_medico):
        assert self.wait_until_find(By.XPATH, patient_profile_constant.MEDICO_FIELD_XPATH).get_attribute('value') == assigned_medico


