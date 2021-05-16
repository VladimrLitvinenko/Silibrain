STAGE_BASE_URL = "https://stg-hospitalprivadopeten.geniusee.space/"
INGRESSA_BUTTON_LOGIN_PAGE = "//span[text()='Ingresa']"

# LOGIN PAGE
LOGIN_EMAIL_INPUT_FIELD = "//input[@name='email']"
LOGIN_PASSWORD_INPUT_FIELD = "//input[@name='password']"
LOGIN_EMAIL_ERROR_MESSAGE = "//p[text()='Usuario no encontrado']"
LOGIN_PASSWORD_ERROR_MESSAGE = "//p[text()='Credenciales no validas']"
AFTER_SUCCESS_LOGIN = "//input[@value='v.litvinenko+admin@geniusee.com']"
LOGIN_FORGOT_PASSWORD_LINK = "//a[@href='#/auth/forgot_password']"

# FORGOT PASSWORD PAGE
FORGOT_PAGE_EMAIL_INPUT_FIELD = "//input[@name='email']"
FORGOT_PAGE_REST_BUTTON = "//span[text()='Reajusta tu Cuenta']"
FORGOT_PAGE_USER_NOT_FOUND_MESSAGE = "//p[text()='Usuario no encontrado']"
FORGOT_PAGE_RESET_PASSWORD_BUTTON = "//span[text()='Reajusta tu Cuenta']"
FORGOT_PAGE_SUCCESS_RESET_MESSAGE = "//p[contains(text(),'El enlace se envió a su correo electrónico permiti')]"

# Valid login
ADMIN_LOGIN = "v.litvinenko+enfermera@geniusee.com"
ADMIN_PASSWORD = "12341234"

TECHLAB_LOGIN = "v.litvinenko+techlab@geniusee.com"
TECHLAB_PASSWORD = "12341234"
