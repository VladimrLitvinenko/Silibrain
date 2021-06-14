import random

CREATE_PATIENT_BUTTON_XPATH = "//span[contains(text(),'Añadir nuevo paciente')]"
CREATE_PATIENT_BUTTON_ON_POP_UP_XPATH = "//span[text()='Agregar']"

# CREATE PATIENT fields on the create tests_patient overlay
FIRST_NAME_FIELD_XPATH = "//div/input[@name='firstName']"
LAST_NAME_FIELD_XPATH = "//div/input[@name='lastName']"
EMAIL_FIELD_XPATH = "//div/input[@name='email']"
PHONE_FIELD_XPATH = "//div/input[@name='phone']"
PAYMENT_FIELD_XPATH = "//div[@id='mui-component-select-paymentType']"
PAYMENT_COEX_OPTION_XPATH = "//li[text()='COEX']"
LIST_OF_PATIENTS_FIRSTMAMES_XPATH = "//tbody[@class='MuiTableBody-root']/tr/td[1]"
SEARCH_TEXTBOX = "//input[@placeholder='Encuentra a paciente']"