import logging
import random
import time

import pytest
from selenium.webdriver.common.by import By

from constants import case_constants
from pages.baseClass import BasePage

"""Для всего класса теперь будет действовать setup fixture"""


class MedRecordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def click_create_med_record_button(self):
        med_record_creation_button = self.wait_until_find(locator_type=By.XPATH, locator="//span[contains(text(),'Agregar record medico nuevo')]")
        med_record_creation_button.click()
        self.logger.debug("med record creation button is clicked")

    def open_med_record_calendar(self):
        """
         - Open med record calendar within med record overlay
         - Click OK to create default med record
        """
        open_med_record_calendar = self.wait_until_find(locator_type=By.XPATH, locator="//label[@id='time-picker-label']/parent::div")
        open_med_record_calendar.click()

        OK_button_within_calendar = self.driver.find_element(By.XPATH, value="//span[text()='OK']")
        OK_button_within_calendar.click()
        self.logger.debug("med record calendar is opened and default date is selected")

    def click_created_button_within_med_record_creation_overlay(self):
        self.driver.find_element(By.XPATH, value="//span[text()='Agregar']").click()

    def create_med_record(self):
        self.click_create_med_record_button()
        self.open_med_record_calendar()
        self.click_created_button_within_med_record_creation_overlay()

    def open_newly_created_med_record(self):
        open_med_record_button = self.wait_until_click(By.XPATH, locator="//span[contains(text(),'Ver récord médico')]")
        open_med_record_button.click()

    def verify_name_of_med_record_placeholder(self):
        self.wait_for_text(locator_type=By.XPATH, locator="//label[text()='Fecha (Nombre del Documento)']", text= 'Fecha (Nombre del Documento)')
