import random


class PatientData:
    variety = str(random.randint(1000, 9999))

    UNIQUE_PATIENT_FIRSTNAME = f"VLADIMIR{variety}"
    VALID_PATIENT_CREATION_DATA = [
        {
         "first_name": F"VLADIMIR{variety}",
         "last_name": "LENIN",
         "email": "879878@GMAIL.COM",
         "phone": "123412341324,",
         }
    ]
