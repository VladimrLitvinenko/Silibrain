import pytest

from pages.patient_page.med_record_page import MedRecordPage


@pytest.mark.usefixtures("setup")
class TestMedRecord:

    def test_placeholder_name(self, create_patient):
        med_record_obj = MedRecordPage(self.driver)
        med_record_obj.click_create_med_record_button()
        med_record_obj.verify_name_of_med_record_placeholder()