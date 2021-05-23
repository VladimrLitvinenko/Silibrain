import random


class UsersData:
    variety = str(random.randint(1000, 9999))
    ADMIN_LOGIN = "v.litvinenko+admin@geniusee.com"
    ADMIN_PASSWORD = "12341234"

    TECHLAB_LOGIN = "v.litvinenko+techlab@geniusee.com"
    TECHLAB_PASSWORD = "12341234"

    ENFERMERA_LOGIN = "v.litvinenko+enfermera@geniusee.com"
    ENFERMERA_PASSWORD = "12341234"

    INVALID_USER_RESTRICTIONS = [
        {"invalid_login": "invladtest@gmail.com", "invalid_password": "invl"},
    ]

    # INPUTS
    FIRST_NAME_INPUT = f"TestFirstName{variety}"
    LAST_NAME_INPUT = f"TestLastName{variety}"
    PHONE_INPUT = f"12345678{variety}"