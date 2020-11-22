from django.core.exceptions import ValidationError
import requests

def validate_email(email):
    response = requests.get(
        'https://isitarealemail.com/api/email/validate',
        params = {"email": email}
    )

    status = response.json()['status']
    if not status == "valid":
        raise ValidationError("L'informazione inserita non corrisponde ad un'email valida")

    else:
        if not "liceovolterra.edu.it" in email:
            raise ValidationError("E' necessario utlizzare la mail istituzionale del L.S.S.Vito Volterra (@liceovolterra.edu.it)")
