import random

CREATE_PATIENT_BUTTON_XPATH = "//span[contains(text(),'Añadir nuevo paciente')]"
CREATE_PATIENT_BUTTON_ON_POP_UP_XPATH = "//span[contains(text(),'Agregar')]"

# CREATE PATIENT fields on the create patient overlay
FIRST_NAME_FIELD_XPATH = "//div/input[@name='firstName']"
LAST_NAME_FIELD_XPATH = "//div/input[@name='lastName']"
EMAIL_FIELD_XPATH = "//div/input[@name='email']"
PHONE_FIELD_XPATH = "//div/input[@name='phone']"
PAYMENT_FIELD_XPATH = "//div[@id='mui-component-select-paymentType']"
PAYMENT_COEX_OPTION_XPATH = "//ul[@role='listbox']/li[5]"
LIST_OF_PATIENTS_FIRSTMAMES = "//tbody[@class='MuiTableBody-root']/tr/td[1]"

# Inputs
VALID_PATIENT_EMAIL = "Email@gmail.com"

variety = str(random.randint(1000, 9999))
UNIQUE_PATIENT_FIRSTNAME = f"TEST firstName {variety}"
