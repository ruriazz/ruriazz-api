import requests
from datetime import datetime
from http import HTTPStatus
from django.conf import settings

def token_validation(token: str) -> bool:
    res = requests.post(
        url='https://api.hcaptcha.com/siteverify',
        data={ 'response':  token, 'secret': settings.HCAPTCHA_SECRET }
    )

    if res.status_code == HTTPStatus.OK:
        json_response = res.json()
        if json_response.get('success') and json_response.get('hostname', '') in settings.HCAPTCHA_ALLOWED_HOSTS:
            submit_challenge = datetime.strptime(json_response['challenge_ts'], "%Y-%m-%dT%H:%M:%S.%fZ")
            if (datetime.now() - submit_challenge).total_seconds() < 7:
                return True
    return False
