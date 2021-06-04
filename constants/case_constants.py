# TEXT

CASE_INITIAL_MESSAGE_MESSAGE = "No hay casos disponibles, cree uno."
CASE_OPENING_OVERLAY_BUTTON_NAME = "Agregar nuevo caso"
FIRST_CHECKBOX_TEXT = "Documento 1 Firmado"
SECOND_CHECKBOX_TEXT = "Documento 2 Firmado"

# ELEMENTS
CASE_INITIAL_MESSAGE_MESSAGE_XPATH = f"//h5[text() = '{CASE_INITIAL_MESSAGE_MESSAGE}']"
CASE_TAB_XPATH = "//span[text()='Casos']"
CASE_OPENING_OVERLAY_BUTTON_XPATH = F"//span[text()='{CASE_OPENING_OVERLAY_BUTTON_NAME}']"
CASE_CALENDAR_OVERLAY_OPENING_XPATH = "//div[@class='MuiInputAdornment-root MuiInputAdornment-positionEnd']/button"
CASE_CALENDAR_SELECTION_BUTTON_XPATH = "//span[text()='OK']"
CASE_BUDGET_DROP_DOWN_LIST_XPATH = "//div[@aria-labelledby='mui-component-select-budget']"

#Buttons
CREATE_CASE_BUTTON_WITHIN_OVERLAY_XPATH = "//span[text() = 'Añadir']/parent::button"
CASE_OPENING_BUTTON_XPATH = "//span[contains(text(),'Ver caso')]"

# Drop down selection
LEVE_CASE_BUDGET_ELEMENT_XPATH = "//ul[@role = 'listbox']/li[1]"


# Checkboxes
FIRST_CHECKBOX_XPATH = F"//span[text()='{FIRST_CHECKBOX_TEXT}']"
SECOND_CHECKBOX_XPATH = F"//span[text()='{SECOND_CHECKBOX_TEXT}']"
