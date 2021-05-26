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
        self.wait_until_click(locator_type=By.XPATH, locator= "//span[text()='Casos']")
        self.logger.debug("Case tab is clicked")

    def open_case_creation_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator= "//span[text()='Agregar nuevo caso']")
        self.logger.debug("Create CASE overlay is opened")

    def open_calendar_within_case_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator= "//div[@class='MuiInputAdornment-root MuiInputAdornment-positionEnd']/button")
        self.logger.debug("Calendar into case overlay is opened")

    def select_default_date_into_case_calendar(self):
        self.wait_until_click(locator_type=By.XPATH, locator= "//span[text()='OK']")
        self.logger.debug("Default Calendar date is selected into case overlay")

    def select_budget_within_dropdown(self):
        click_budget_drop_down = self.driver.find_element(By.XPATH, value="//div[@id='mui-component-select-budget']")
        click_budget_drop_down.click()

        self.wait_until_click(locator_type=By.XPATH, locator= case_constants.LEVE_SELLECTION_WIHIN_CASE_XPATH)
        self.logger.debug(f"budget is selected into dropdown")

    def check_first_check_box(self):
        first_checkbox = self.driver.find_element(By.XPATH, value="//span[text()='Documento 1 Firmado']")
        first_checkbox.click()
        self.logger.debug("checkbox 1 is checked")

    def check_second_check_box(self):
        first_checkbox = self.driver.find_element(By.XPATH, value="//span[text()='Documento 2 Firmado']")
        first_checkbox.click()
        self.logger.debug("checkbox 2 is checked")

    def click_create_case_button_within_case_creation_overlay(self):
        create_case_button_within_overlay =  self.driver.find_element(By.XPATH, value="//span[text() = 'Añadir']")
        create_case_button_within_overlay.click()
        self.logger.debug("creation button is clicked within case creation overlay")

    def open_newly_created_case(self):
        created_case = self.wait_until_find(locator_type=By.XPATH, locator= "//span[contains(text(),'Ver caso')]")
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

