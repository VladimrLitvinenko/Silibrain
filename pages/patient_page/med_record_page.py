import datetime
import logging
import random
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    def verify_date_of_created_med_record_is_displayed(self):
        self.wait_for_text(locator_type=By.XPATH, locator=med_record_constants.TIME_ON_CREATED_MED_RECORD_XPATH, text=med_record_constants.CURRENT_TIME_TEXT)
        self.logger.debug(f"Time on the created med record = {med_record_constants.CURRENT_TIME_TEXT}")

    def verify_name_of_med_record_placeholder(self):
        self.wait_for_text(locator_type=By.XPATH, locator=med_record_constants.PLACEHOLDER_WITHIN_MED_RECORD_CREATION_OVERLAY_XPATH,
                           text= med_record_constants.TEXT_WITHIN_MED_RECORD_CREATION_OVERLAY)
        self.logger.debug(f"The text wihin placeholder is {med_record_constants.TEXT_WITHIN_MED_RECORD_CREATION_OVERLAY}")



    def send_data_into_nota_de_evolucion_medica(self, sent_data):
        nota_de_evolucion_medica_field = self.wait_until_find(By.XPATH, med_record_constants.NOTA_DE_EVOLUCION_FIELD_XPATH)
        nota_de_evolucion_medica_field.send_keys(sent_data)
        self.logger.debug(f"data is sent into the evolucion medica field and = {sent_data}")

    def click_create_button_for_nota_de_evolucion_medica(self):
        nota_de_evolucion_medica_button = self.driver.find_element(By.XPATH, med_record_constants.NOTA_DE_EVOLUCION_BUTTON_XPATH)
        nota_de_evolucion_medica_button.click()
        self.logger.debug(f" 'Create' Button for NOTAS DE EVOLUCION MEDICA is clicked")

    def verify_nota_de_evolucion_medica_comment_saved(self, data):
        comment = self.wait_until_find(locator_type=By.XPATH, locator=med_record_constants.NOTA_DE_EVOLUCION_COMMENT_XPATH)
        self.logger.debug(f"comment text into nota de evolucion field ={comment.text} data {data}")
        assert comment.text == data

    def create_nota_de_evolucion_medica(self, data):
        self.send_data_into_nota_de_evolucion_medica(data)
        self.click_create_button_for_nota_de_evolucion_medica()
        self.verify_nota_de_evolucion_medica_comment_saved(data)

    def send_data_into_resumen_de_ordenes_field(self, sent_data):
        resumen_de_ordenes_field = self.wait_until_find(By.XPATH, med_record_constants.RESUMEN_DE_ORDENES_FIELD_XPATH)
        resumen_de_ordenes_field.send_keys(sent_data)
        self.logger.debug(f"data is sent into the resumen de ordenes field and = {sent_data}")

    def click_create_button_for_resumen_de_ordenes(self):
        resumen_de_ordenes_button = self.driver.find_element(By.XPATH, med_record_constants.RESUMEN_DE_ORDENES_BUTTON_XPATH)
        resumen_de_ordenes_button.click()
        self.logger.debug(f" 'Create' Button for RESUMEN DE ORDENES is clicked")

    def verify_resumen_de_ordenes_saved(self, data):
        comment = self.wait_until_find(locator_type=By.XPATH, locator=med_record_constants.RESUMEN_DE_ORDENES_COMMENT_XPATH)
        self.logger.debug(f"comment text into RESUMEN DE ORDENES field ={comment.text} data {data}")
        assert comment.text == data


    def create_resumen_de_ordenes(self, data):
        self.send_data_into_resumen_de_ordenes_field(data)
        self.click_create_button_for_resumen_de_ordenes()
        self.verify_resumen_de_ordenes_saved(data)

    def send_data_into_notas_de_enfermeria_field(self, sent_data):
        resumen_de_ordenes_field = self.wait_until_find(By.XPATH, med_record_constants.NOTAS_DE_ENFERMERIA_FIELD_XPATH)
        resumen_de_ordenes_field.send_keys(sent_data)
        self.logger.debug(f"data is sent into the notas de enfermeria field and = {sent_data}")

    def click_create_button_for_notas_de_enfermeria(self):
        resumen_de_ordenes_button = self.driver.find_element(By.XPATH,
                                                             med_record_constants.NOTAS_DE_ENFERMERIA_BUTTON_XPATH)
        resumen_de_ordenes_button.click()
        self.logger.debug(f" 'Create' Button for NOTAS DE ENFERMERIA is clicked")

    def verify_notas_de_enfermeria_saved(self, data):
        comment = self.wait_until_find(locator_type=By.XPATH,
                                       locator=med_record_constants.NOTAS_DE_ENFERMERIA_COMMENT_XPATH)
        self.logger.debug(f"comment text into NOTAS DE ENFERMERIA field ={comment.text} data {data}")
        assert comment.text == data

    def create_notas_de_enfermeria(self, data):
        self.send_data_into_notas_de_enfermeria_field(data)
        self.click_create_button_for_notas_de_enfermeria()
        self.verify_notas_de_enfermeria_saved(data)

    def send_data_into_signos_vitales_fields(self, data):
        signos_vitales_fields_list = self.driver.find_elements(By.XPATH, value=med_record_constants.SIGNOS_VITALES_LIST_OF_FIELDS_XPATH)
        for each_field in signos_vitales_fields_list:
            each_field.send_keys(data)
        self.logger.debug(f"Comment text into SIGNOS VITALES field is sent and = {data}")

    def click_create_button_for_signos_vitales_field(self):
        signos_vitales_button= self.driver.find_element(By.XPATH, value=med_record_constants.SIGNOS_VITALES_BUTTON_XPATH)
        signos_vitales_button.click()
        self.logger.debug(f"SIGNOS VITALES create comment is clicked")

    def verify_SIGNOS_VITALES_comment_saved(self, data):
        comment_list = self.driver.find_elements(By.XPATH, med_record_constants.SIGNOS_VITALES_COMMENT_XPATH)
        for each_feild  in comment_list:
            assert each_feild.text == data
            self.logger.info(f"comment text into SIGNOS VITALES field ={each_feild.text} data {data}")
        assert len(comment_list) == 8
        self.logger.debug(f"Added comments = actual result: {len(comment_list)} expected result = 8")

    def create_SIGNOS_VITALES_comment(self, data):
        self.send_data_into_signos_vitales_fields(data)
        self.click_create_button_for_signos_vitales_field()
        self.verify_SIGNOS_VITALES_comment_saved(data)

    def send_data_into_examenes_laboratorio_field(self, sent_data):
        examenes_laboratoria_field = self.wait_until_find(By.XPATH, med_record_constants.EXAMENES_LABORATORIO_FIELD_XPATH)
        examenes_laboratoria_field.send_keys(sent_data)
        self.logger.debug(f"data is sent into the EXAMENES LABORATORIA field and = {sent_data}")

    def click_create_button_for_examenes_laboratorio(self):
        examenes_laboratoria_button = self.driver.find_element(By.XPATH,
                                                             med_record_constants.EXAMENES_LABORATORIO_BUTTON_XPATH)
        examenes_laboratoria_button.click()
        self.logger.debug(f" 'Create' Button for EXAMENES LABORATORIA is clicked")

    def verify_examenes_laboratorio_saved(self, data):
        comment = self.wait_until_find(locator_type=By.XPATH,
                                       locator=med_record_constants.EXAMENES_LABORATORIO_COMMENT_XPATH)
        self.logger.debug(f"comment text into EXAMENES LABORATORIA field ={comment.text} data {data}")
        assert comment.text == data

    def create_EXAMENES_LABORATORIA_comment(self, data):
        self.send_data_into_examenes_laboratorio_field(data)
        self.click_create_button_for_examenes_laboratorio()
        self.verify_examenes_laboratorio_saved(data)


    def send_data_into_examenes_radiologio_field(self, sent_data):
        examenes_laboratoria_field = self.wait_until_find(By.XPATH, med_record_constants.EXAMENES_RADIOLOGIA_FIELD_XPATH)
        examenes_laboratoria_field.send_keys(sent_data)
        self.logger.debug(f"data is sent into the EXAMENES RADIOLOGIO field and = {sent_data}")

    def click_create_button_for_examenes_radiologio(self):
        examenes_laboratoria_button = self.driver.find_element(By.XPATH,
                                                             med_record_constants.EXAMENES_RADIOLOGIA_BUTTON_XPATH)
        examenes_laboratoria_button.click()
        self.logger.debug(f" 'Create' Button for EXAMENES RADIOLOGIO is clicked")

    def verify_examenes_radiologio_saved(self, data):
        comment = self.wait_until_find(locator_type=By.XPATH,
                                       locator=med_record_constants.EXAMENES_RADIOLOGIA_COMMENT_XPATH)
        self.logger.debug(f"comment text into EXAMENES RADIOLOGIO field ={comment.text} data {data}")
        assert comment.text == data

    def create_EXAMENES_RADIOLOGIO_comment(self, data):
        self.send_data_into_examenes_radiologio_field(data)
        self.click_create_button_for_examenes_radiologio()
        self.verify_examenes_radiologio_saved(data)

    def send_data_into_control_de_medicamentos_fields(self, data):
        control_de_medicamentos_fields_list = self.driver.find_elements(By.XPATH, value=med_record_constants.CONTROL_DE_MEDICAMENTOS_LIST_OF_FIELDS_XPATH)
        for each_field in control_de_medicamentos_fields_list:
            each_field.send_keys(data)
        self.logger.debug(f"Comment text into control de medicamentos field is sent and = {data}")

    def click_create_button_for_control_de_medicamentos_field(self):
        signos_vitales_button= self.driver.find_element(By.XPATH, value=med_record_constants.CONTROL_DE_MEDICAMENTOS_BUTTON_XPATH)
        signos_vitales_button.click()
        self.logger.debug(f"control de medicamentos create comment is clicked")

    def verify_control_de_medicamentos_comment_saved(self, data):
        time.sleep(3)
        comment_list = self.driver.find_elements(By.XPATH, med_record_constants.CONTROL_DE_MEDICAMENTOS_COMMENT_XPATH)
        for each_feild  in comment_list:
            assert each_feild.text == data
            self.logger.info(f"comment text into control de medicamentos field ={each_feild.text} data {data}")
        assert len(comment_list) == 6
        self.logger.info(f"Added comments = actual result: {len(comment_list)} expected result = 6")

    def create_control_de_medicamentos_comment(self, data):
        self.send_data_into_control_de_medicamentos_fields(data)
        self.click_create_button_for_control_de_medicamentos_field()
        self.verify_control_de_medicamentos_comment_saved(data)

    def click_edit_button_within_opened_comment_overlay(self):
        self.wait_until_click(locator_type=By.XPATH, locator=med_record_constants.EDIT_BUTTON_FOR_OPENED_COMMENT_OVERLAY)

    def verify_particullar_comment_is_updated(self, data, updated_comment_xpath):
        comment = self.wait_until_find(locator_type=By.XPATH, locator=updated_comment_xpath)
        self.logger.debug(f"comment text is updated ={comment.text} data {data}")
        assert comment.text == data

    def verify_resumen_de_orderes_comment_is_updated(self, data):
        comment = self.wait_until_find(locator_type=By.XPATH, locator=med_record_constants.UPDATED_RESUMEN_DE_ORDENES_COMMENT_XPATH)
        self.logger.debug(f"comment text into nota de evolucion field ={comment.text} data {data}")
        assert comment.text == data

    def update_particullar_nota(self, updated_data, comment_xpath, updated_comment_xpath):
        """Click edit button for the exist comment"""
        comment = self.wait_until_find(locator_type=By.XPATH,
                                       locator=comment_xpath)
        edit_button = comment.find_element(By.XPATH, value=med_record_constants.UPDATE_BUTTON_FOR_COMMENT_XPATH)
        edit_button.click()
        self.logger.debug(f"Edit button is clicked on the exist comment")

        """Clear the displayed textbox within overlay"""
        nota_de_evolucion_medica_field = self.wait_until_find(By.XPATH, med_record_constants.UPDATE_TEXT_BOX_FOR_OPENED_COMMENT_XPATH)
        nota_de_evolucion_medica_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        self.logger.debug(f"Field is cleared")

        """Send the updated data within current field"""
        nota_de_evolucion_medica_field.send_keys(updated_data)
        self.logger.debug(f"Updated data is sent and = {updated_data}")

        """Click edit button within overlay"""
        self.click_edit_button_within_opened_comment_overlay()
        self.logger.debug(f"Edit button is clicked within overlay")

        """Verify the field is edited"""
        self.verify_particullar_comment_is_updated(updated_data, updated_comment_xpath=updated_comment_xpath)
        self.logger.debug(f"Comment is observed and updated data = {updated_data} is verified")









