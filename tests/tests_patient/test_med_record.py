import time

import pytest

from constants import med_record_constants
from pages.patient_page.med_record_page import MedRecordPage
from test_data import med_record_data


@pytest.mark.usefixtures("setup")
class TestMedRecord:

    def test_placeholder_name(self, create_case_as_admin):
        med_record_obj = MedRecordPage(self.driver)
        """
        - Open CREATION MED RECORD overlay
        - Verify the proper placeholder is displayed
        """
        med_record_obj.click_create_med_record_button()
        self.logger.info("'Create med' record button is clicked")
        med_record_obj.verify_name_of_med_record_placeholder()
        self.logger.info("Med record placeholder is verified")

    def test_med_record_is_created(self, create_case_as_admin):
        med_record_obj = MedRecordPage(self.driver)
        med_record_obj.create_med_record()
        self.logger.info("Med record is created")
        med_record_obj.verify_date_of_created_med_record_is_displayed()
        self.logger.info("Med record is created and todays date is displayed there")

    def test_all_notas_are_added(self, create_case_as_admin):
        """
        - Create med record
        - Open med record
        - Create nota de evolucion and verify it is created
        - Create SIGNOS VITALES and verify it is created and  = 8
        - Create CONTROL MEDICAMENTOS and verify it is created and  = 6
        """
        med_record_obj = MedRecordPage(self.driver)
        med_record_obj.create_med_record()
        self.logger.info("Med record is created")
        med_record_obj.open_newly_created_med_record()
        self.logger.info("Med record is Opened")

        med_record_obj.create_nota_de_evolucion_medica(med_record_data.notas_data)
        self.logger.info(f"Med nota de evolucion medica is added an verified = {med_record_data.notas_data}")
        med_record_obj.create_resumen_de_ordenes(med_record_data.resumen_de_ordenes_data)
        self.logger.info(f"RESUMEN DE ORDERES is added an verified = {med_record_data.resumen_de_ordenes_data}")
        med_record_obj.create_notas_de_enfermeria(med_record_data.notas_de_enfermeria_data)
        self.logger.info(f"NOTAS DE ENFERMERIA is added an verified = {med_record_data.notas_de_enfermeria_data}")
        med_record_obj.create_SIGNOS_VITALES_comment(med_record_data.signos_vitales_data)
        self.logger.info(f"SIGNOS VITALES comment is added an verified = {med_record_data.signos_vitales_data}")
        med_record_obj.create_control_de_medicamentos_comment(med_record_data.control_medicamentos_data)
        self.logger.info(
            f"CONTROL DE MEDICAMENTOS comment is added an verified = {med_record_data.control_medicamentos_data}")
        med_record_obj.create_EXAMENES_LABORATORIA_comment(data=med_record_data.examen_laboratoria_data)
        self.logger.info(
            f"EXAMENES LABORATORIA comment is added an verified = {med_record_data.examen_laboratoria_data}")
        med_record_obj.create_EXAMENES_RADIOLOGIO_comment(med_record_data.examen_radiologia_data)
        self.logger.info(
            f"EXAMENES RADIOLOGIO comment is added an verified = {med_record_data.examen_radiologia_data}")

    def test_all_notas_are_updated(self, create_case_as_admin):
        """
        - Create med record
        - Open med record
        - Create nota de evolucion and verify it is created
        - Create SIGNOS VITALES and verify it is created and  = 8
        - Create CONTROL MEDICAMENTOS and verify it is created and  = 6
        - Update all created notas
        """
        med_record_obj = MedRecordPage(self.driver)
        med_record_obj.create_med_record()
        self.logger.info("Med record is created")
        med_record_obj.open_newly_created_med_record()
        self.logger.info("Med record is Opened")

        med_record_obj.create_nota_de_evolucion_medica(med_record_data.notas_data)
        self.logger.info(f"Med nota de evolucion medica is added an verified = {med_record_data.notas_data}")
        med_record_obj.update_particullar_nota(updated_data=med_record_data.notas_updated_data,
                                               comment_xpath=med_record_constants.NOTA_DE_EVOLUCION_COMMENT_XPATH,
                                               updated_comment_xpath=med_record_constants.UPDATED_NOTA_DE_EVOLUCION_COMMENT_XPATH)
        self.logger.info(f"Notas is updated and = {med_record_data.notas_updated_data}")

        med_record_obj.create_resumen_de_ordenes(med_record_data.resumen_de_ordenes_data)
        self.logger.info(f"RESUMEN DE ORDERES is added an verified = {med_record_data.resumen_de_ordenes_data}")
        med_record_obj.update_particullar_nota(updated_data=med_record_data.resumen_de_ordenes_updated_data,
                                               comment_xpath=med_record_constants.RESUMEN_DE_ORDENES_COMMENT_XPATH,
                                               updated_comment_xpath=med_record_constants.UPDATED_RESUMEN_DE_ORDENES_COMMENT_XPATH)
        self.logger.info(f"RESUMEN DE ORDERES is updated and = {med_record_data.resumen_de_ordenes_updated_data}")

        med_record_obj.create_notas_de_enfermeria(med_record_data.notas_de_enfermeria_data)
        self.logger.info(f"NOTAS DE ENFERMERIA is added an verified = {med_record_data.notas_de_enfermeria_data}")
        med_record_obj.create_SIGNOS_VITALES_comment(med_record_data.signos_vitales_data)
        self.logger.info(f"SIGNOS VITALES comment is added an verified = {med_record_data.signos_vitales_data}")
        med_record_obj.create_control_de_medicamentos_comment(med_record_data.control_medicamentos_data)
        self.logger.info(f"CONTROL DE MEDICAMENTOS comment is added an verified = {med_record_data.control_medicamentos_data}")
        med_record_obj.create_EXAMENES_LABORATORIA_comment(data=med_record_data.examen_laboratoria_data)
        self.logger.info(f"EXAMENES LABORATORIA comment is added an verified = {med_record_data.examen_laboratoria_data}")
        med_record_obj.create_EXAMENES_RADIOLOGIO_comment(med_record_data.examen_radiologia_data)
        self.logger.info(
            f"EXAMENES RADIOLOGIO comment is added an verified = {med_record_data.examen_radiologia_data}")
