import logging
import random
import time

import pytest
from selenium.webdriver.common.by import By

from constants import case_constants
from pages.baseClass import BasePage

"""Для всего класса теперь будет действовать setup fixture"""


class CaseTabPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def click_case_tab(self):
        self.wait_until_click(locator_type=By.XPATH, locator= case_constants.CASE_TAB_XPATH)
        self.logger.debug("Case tab is clicked")

    def verify_empty_case_tab_message_is_displayed(self):
        empty_case_tab_message = self.wait_until_find(locator_type=By.XPATH, locator=case_constants.CASE_INITIAL_MESSAGE_MESSAGE_XPATH)
        assert empty_case_tab_message.text == case_constants.CASE_INITIAL_MESSAGE_MESSAGE

    def open_case_creation_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator= case_constants.CASE_OPENING_OVERLAY_BUTTON_XPATH)
        self.logger.debug("Create CASE overlay is opened")

    def open_calendar_within_case_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator= case_constants.CASE_CALENDAR_OVERLAY_OPENING_XPATH)
        self.logger.debug("Calendar into case overlay is opened")

    def select_default_date_into_case_calendar(self):
        self.wait_until_click(locator_type=By.XPATH, locator= case_constants.CASE_CALENDAR_SELECTION_BUTTON_XPATH)
        self.logger.debug("Default Calendar date is selected into case overlay")

    def select_budget_within_dropdown(self):
        click_budget_drop_down = self.driver.find_element(By.XPATH, value=case_constants.CASE_BUDGET_DROP_DOWN_LIST_XPATH)
        click_budget_drop_down.click()

        self.wait_until_click(locator_type=By.XPATH, locator= case_constants.LEVE_CASE_BUDGET_ELEMENT_XPATH)
        self.logger.debug(f"budget is selected into dropdown")

    def check_first_check_box(self):
        first_checkbox = self.driver.find_element(By.XPATH, value=case_constants.FIRST_CHECKBOX_XPATH)
        first_checkbox.click()
        self.logger.debug("checkbox 1 is checked")

    def check_second_check_box(self):
        first_checkbox = self.driver.find_element(By.XPATH, value=case_constants.SECOND_CHECKBOX_XPATH)
        first_checkbox.click()
        self.logger.debug("checkbox 2 is checked")

    def click_create_case_button_within_case_creation_overlay(self):
        create_case_button_within_overlay = self.driver.find_element(By.XPATH, value=case_constants.CREATE_CASE_BUTTON_WITHIN_OVERLAY_XPATH)
        create_case_button_within_overlay.click()
        self.logger.debug("creation button is clicked within case creation overlay")

    def open_newly_created_case(self):
        created_case = self.wait_until_find(locator_type=By.XPATH, locator= case_constants.CASE_OPENING_BUTTON_XPATH)
        created_case.click()
        self.logger.debug("created case is opened")

    def create_case_with_default_date(self):
        """
        - overlay case creaetion is clicked
        - default case date is selected
        """

        self.open_case_creation_overlay()
        self.open_calendar_within_case_overlay()
        self.select_default_date_into_case_calendar()
        self.select_budget_within_dropdown()
        self.check_first_check_box()
        self.check_second_check_box()
        self.click_create_case_button_within_case_creation_overlay()

    def create_3_cases_with_default_dates(self):
        i = 1
        """
        - Add 3 CASES
        - Add ech case to the list_of_buttons
        - verify length of list_of_buttons == 3"""
        list_of_buttons = list()
        while i <= 3:
            self.create_case_with_default_date()

            i += 1
            time.sleep(1)
            list_of_buttons.append(case_constants.CASE_OPENING_BUTTON_XPATH)
        self.logger.debug(
            f"Actual={len(list_of_buttons)} and expected = 3 cases are created and validated")
        assert len(list_of_buttons) == 3

    def verify_craete_case_button_is_disabled(self):
        creation_button = self.driver.find_element(By.XPATH,
                                                   value=case_constants.CREATE_CASE_BUTTON_WITHIN_OVERLAY_XPATH)
        assert creation_button.is_enabled() == False

    def click_remove_case_button(self):
        self.wait_until_click(By.XPATH, case_constants.CASE_REMOVE_BUTTON_XPATH)
        self.wait_until_click(By.XPATH, case_constants.CASE_REMOVE_BUTTON_WITHIN_OVERLAY_XPATH)
        self.logger.debug(
            f" 'Remove case' button is clicked ")





