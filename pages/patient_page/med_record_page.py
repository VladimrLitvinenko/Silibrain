import logging
import random
import time

import pytest
from selenium.webdriver.common.by import By

from constants import case_constants, med_record_constants
from pages.baseClass import BasePage

"""Для всего класса теперь будет действовать setup fixture"""


class MedRecordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def click_create_med_record_button(self):
        med_record_creation_button = self.wait_until_find(locator_type=By.XPATH, locator=med_record_constants.CREATE_MED_RECORD_BUTTON_XPATH)
        med_record_creation_button.click()
        self.logger.debug("med record creation button is clicked")

    def open_med_record_calendar(self):
        """
         - Open med record calendar within med record overlay
         - Click OK to create default med record
        """
        open_med_record_calendar = self.wait_until_find(locator_type=By.XPATH, locator=med_record_constants.OPEN_MED_RECORD_CALENDAR_XPATH)
        open_med_record_calendar.click()

        OK_button_within_calendar = self.driver.find_element(By.XPATH, value=med_record_constants.OK_BUTTON_WITHIN_MED_RECORD_CALENDAR_XPATH)
        OK_button_within_calendar.click()
        self.logger.debug("med record calendar is opened and default date is selected")

    def click_created_button_within_med_record_creation_overlay(self):
        create_button_within_med_record_overlay = self.driver.find_element(By.XPATH, value=med_record_constants.CREATE_BUTTON_WITHIN_MED_RECORD_OVERLAY_XPATH)
        create_button_within_med_record_overlay.click()

    def create_med_record(self):
        self.click_create_med_record_button()
        self.open_med_record_calendar()
        self.click_created_button_within_med_record_creation_overlay()

    def open_newly_created_med_record(self):
        open_med_record_button = self.wait_until_click(By.XPATH, locator=med_record_constants.OPEN_MED_RECORD_BUTTON_XPATH)
        open_med_record_button.click()

    def verify_name_of_med_record_placeholder(self):
        self.wait_for_text(locator_type=By.XPATH, locator=med_record_constants.PLACEHOLDER_WITHIN_MED_RECORD_CREATION_OVERLAY_XPATH,
                           text= med_record_constants.TEXT_WITHIN_MED_RECORD_CREATION_OVERLAY)
