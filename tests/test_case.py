"""Case page tests"""
import time

import pytest
from selenium.webdriver.common.by import By

from constants import login_constants, case_constants, patient_list_constant
from constants.case_constants import CASE_INITIAL_MESSAGE_MESSAGE
from pages.login_page import LoginPage
from pages.patient_case_tab_page import CaseTabPage
from pages.patient_list_page import PatientsListPage
from test_data import users_data
from test_data.users_data import UsersData


@pytest.mark.usefixtures("setup")
class TestStartPage():

    @pytest.fixture(params=UsersData.INVALID_USER_RESTRICTIONS)
    def get_invalid_Data(self, request):
        return request.param

    def test_empty_CASE_message_is_displayed(self, create_patient):
        """
         - Open case tab
         - Click create case button
         - Verify the special message is displayed
        """
        case_tab_page_obj = CaseTabPage(self.driver)
        case_tab_page_obj.click_case_tab()
        case_tab_page_obj.verify_empty_case_tab_message_is_displayed()

    def test_create_3_cases(self, create_patient):
        """
        - Open case tab
        - Create 3 default cases
        """
        case_tab_page_obj = CaseTabPage(self.driver)
        case_tab_page_obj.click_case_tab()
        case_tab_page_obj.create_3_cases_with_default_dates()
        self.logger.info("3 CASES are created and validated")

    def test_create_button_is_disabled_if_first_check_box_selected(self, create_patient):
        """
        - Open case tab
        - Open case creation overlay
        - Open calendar within case overlay
        - Select default date within calendar
        - Select budget
        - Verify CREATE button is disabled
        - Click first checkbox
        - Verify CREATE button is disabled
        """
        case_tab_page_obj = CaseTabPage(self.driver)
        case_tab_page_obj.click_case_tab()
        case_tab_page_obj.open_case_creation_overlay()
        case_tab_page_obj.open_calendar_within_case_overlay()
        case_tab_page_obj.select_default_date_into_case_calendar()
        case_tab_page_obj.select_budget_within_dropdown()
        case_tab_page_obj.check_first_check_box()
        case_tab_page_obj.verify_craete_case_button_is_disabled()

    def test_create_button_is_disabled_if_second_check_box_selected(self, create_patient):
        """
        - Open case tab
        - Open case creation overlay
        - Open calendar within case overlay
        - Select default date within calendar
        - Select budget
        - Verify CREATE button is disabled
        - Click first checkbox
        - Verify CREATE button is disabled
        """
        case_tab_page_obj = CaseTabPage(self.driver)
        case_tab_page_obj.click_case_tab()
        case_tab_page_obj.open_case_creation_overlay()
        case_tab_page_obj.open_calendar_within_case_overlay()
        case_tab_page_obj.select_default_date_into_case_calendar()
        case_tab_page_obj.select_budget_within_dropdown()
        case_tab_page_obj.check_second_check_box()
        case_tab_page_obj.verify_craete_case_button_is_disabled()

    def test_create_button_is_disabled_if_check_boxes_are_unchecked(self, create_patient):
        """
        - Open case tab
        - Open case creation overlay
        - Open calendar within case overlay
        - Select default date within calendar
        - Select budget
        - Verify CREATE button is disabled
        - Click first checkbox
        - Verify CREATE button is disabled
        """
        case_tab_page_obj = CaseTabPage(self.driver)
        case_tab_page_obj.click_case_tab()
        case_tab_page_obj.open_case_creation_overlay()
        case_tab_page_obj.open_calendar_within_case_overlay()
        case_tab_page_obj.select_default_date_into_case_calendar()
        case_tab_page_obj.select_budget_within_dropdown()
        case_tab_page_obj.check_second_check_box()
        case_tab_page_obj.check_first_check_box()
        case_tab_page_obj.check_first_check_box()
        case_tab_page_obj.verify_craete_case_button_is_disabled()

    def test_case_is_able_to_be_removed(self, create_patient):
        case_tab_page_obj = CaseTabPage(self.driver)
        case_tab_page_obj.click_case_tab()
        case_tab_page_obj.create_case_with_default_date()
        case_tab_page_obj.open_newly_created_case()
        case_tab_page_obj.click_remove_case_button()
        case_tab_page_obj.verify_empty_case_tab_message_is_displayed()

