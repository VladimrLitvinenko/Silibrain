import logging

from selenium.webdriver.common.by import By

from constants import patient_profile_constant
from pages.baseClass import BaseTest


class PatientProfilePage(BaseTest):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_remove_button(self):
        remove_patient_button = self.driver.find_element(By.XPATH, value=patient_profile_constant.REMOVE_PATIENT_XPATH)
        remove_patient_button.click()
