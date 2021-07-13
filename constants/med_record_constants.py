# texts
from pages import baseClass
from test_data import med_record_data

CURRENT_TIME_TEXT = baseClass.current_time()
TEXT_WITHIN_MED_RECORD_CREATION_OVERLAY = 'Fecha (Nombre del Documento)'

# XPATH elements
CREATE_MED_RECORD_BUTTON_XPATH = "//span[contains(text(),'Agregar record medico nuevo')]"
OPEN_MED_RECORD_CALENDAR_XPATH = "//label[@id='time-picker-label']/parent::div"
OK_BUTTON_WITHIN_MED_RECORD_CALENDAR_XPATH = "//span[text()='OK']"
CREATE_BUTTON_WITHIN_MED_RECORD_OVERLAY_XPATH = "//span[text()='Agregar']"
OPEN_MED_RECORD_BUTTON_XPATH = "//span[contains(text(),'Ver récord médico')]"
PLACEHOLDER_WITHIN_MED_RECORD_CREATION_OVERLAY_XPATH = F"//label[text()='{TEXT_WITHIN_MED_RECORD_CREATION_OVERLAY}']"

TIME_ON_CREATED_MED_RECORD_XPATH = f"//p[text()='{baseClass.current_time()}']"

# FIELDS
NOTA_DE_EVOLUCION_FIELD_XPATH = "//textarea[@name='medicalEvolutionNote.text']"
RESUMEN_DE_ORDENES_FIELD_XPATH = "//textarea[@name='orderSummaryAlt.text']"
NOTAS_DE_ENFERMERIA_FIELD_XPATH = "//span[text()='Notas de Enfermeria']/parent::legend/parent::fieldset/parent::div/textarea"
SIGNOS_VITALES_LIST_OF_FIELDS_XPATH = "//h5[text()='Signos vitales']/parent::div/div/div/div/div/input"
CONTROL_DE_MEDICAMENTOS_LIST_OF_FIELDS_XPATH = "//h5[text()='Control de Medicamentos']/parent::div/div/div/div/div/input"
EXAMENES_LABORATORIO_FIELD_XPATH = "//h5[text()='Link a Examenes de Laboratorio']/parent::div/div/div/input"
EXAMENES_RADIOLOGIA_FIELD_XPATH = "//h5[text()='Link a Examenes de Radiologia']/parent::div/div/div/input"

# BUTTONS
NOTA_DE_EVOLUCION_BUTTON_XPATH = "//h5[text()='Nota de Evolución Medica']/parent::div/div[2]/button"
RESUMEN_DE_ORDENES_BUTTON_XPATH= "//h5[text()='Resumen de órdenes']/parent::div/div[2]/button"
NOTAS_DE_ENFERMERIA_BUTTON_XPATH = "//h5[text()='Notas de Enfermeria']/parent::div/div/div[2]/button/span"
SIGNOS_VITALES_BUTTON_XPATH = "//h5[text()='Signos vitales']/parent::div/div[2]/button"
CONTROL_DE_MEDICAMENTOS_BUTTON_XPATH = "//h5[text()='Control de Medicamentos']/parent::div/div[2]/button"
EXAMENES_LABORATORIO_BUTTON_XPATH = "//h5[text()='Link a Examenes de Laboratorio']/parent::div/div[2]/button"
EXAMENES_RADIOLOGIA_BUTTON_XPATH = "//h5[text()='Link a Examenes de Radiologia']/parent::div/div[2]/button"

#CREATED COMMENTS
NOTA_DE_EVOLUCION_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.notas_data}')]"
RESUMEN_DE_ORDENES_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.resumen_de_ordenes_data}')]"
SIGNOS_VITALES_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.signos_vitales_data}')]"
CONTROL_DE_MEDICAMENTOS_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.control_medicamentos_data}')]"
NOTAS_DE_ENFERMERIA_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.notas_de_enfermeria_data}')]"
EXAMENES_LABORATORIO_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.examen_laboratoria_data}')]"
EXAMENES_RADIOLOGIA_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.examen_radiologia_data}')]"

#UPDATED COMMENTS
UPDATED_NOTA_DE_EVOLUCION_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.notas_updated_data}')]"
UPDATED_RESUMEN_DE_ORDENES_COMMENT_XPATH = f"//p[contains(text(),'{med_record_data.resumen_de_ordenes_updated_data}')]"


# UPDATE BUTTON FOR COMMENTS
UPDATE_BUTTON_FOR_COMMENT_XPATH = "parent::div/div/button[1]/span"

# OPENED TEXTBOX FOR COMMENTS OVERLAY
UPDATE_TEXT_BOX_FOR_OPENED_COMMENT_XPATH = "//textarea[@name='text']"

# EDIT BUTTON FOR COMMENTS OVERLAY
EDIT_BUTTON_FOR_OPENED_COMMENT_OVERLAY = "//span[contains(text(),'Editar')]"

