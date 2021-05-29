STAGE_BASE_URL = "https://stg-hospitalprivadopeten.geniusee.space/"

# VALIDATION TEXT
FORGOT_PAGE_SUCCESS_RESET_MESSAGE_TEXT = 'El enlace se envió a su correo electrónico permiti'
INVALID_EMAIL_TEXT = 'Usuario no encontrado'
INVALID_PASSWORD_TEXT = 'Credenciales no validas'
SUCCESS_RESSET_PASSWORD_TEXT = 'El enlace se envió a su correo electrónico permitiendo configurar su contraseña'

# BUTTONS
INGRESSA_BUTTON_LOGIN_PAGE = "//span[text()='Ingresa']"

# LOGIN PAGE
LOGIN_EMAIL_INPUT_FIELD_XPATH = "//input[@name='email']"
LOGIN_PASSWORD_INPUT_FIELD_XPATH = "//input[@name='password']"
LOGIN_EMAIL_ERROR_MESSAGE_XPATH = f"//p[text()='{INVALID_EMAIL_TEXT}']"
LOGIN_PASSWORD_ERROR_MESSAGE_XPATH = f"//p[text()='{INVALID_PASSWORD_TEXT}']"
AFTER_SUCCESS_LOGIN_XPATH = "//input[@value='v.litvinenko+admin@geniusee.com']"
LOGIN_FORGOT_PASSWORD_LINK_XPATH = "//a[@href='#/auth/forgot_password']"

# FORGOT PASSWORD PAGE
FORGOT_PAGE_EMAIL_INPUT_FIELD_XPATH = "//input[@name='email']"
FORGOT_PAGE_REST_BUTTON_XPATH = "//span[text()='Reajusta tu Cuenta']"
FORGOT_PAGE_USER_NOT_FOUND_MESSAGE_XPATH = f"//p[text()='{INVALID_EMAIL_TEXT}']"
FORGOT_PAGE_RESET_PASSWORD_BUTTON_XPATH = "//span[text()='Reajusta tu Cuenta']"
FORGOT_PAGE_SUCCESS_RESET_MESSAGE_XPATH = F"//p[(text() = '{SUCCESS_RESSET_PASSWORD_TEXT}')]"



