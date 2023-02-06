import requests
from datetime import datetime, timedelta
from rest_framework import serializers
from configs.settings import ALLOWED_HOSTS, CAPTCHA_SECRET


class Validator:
    class PostSubmitContact(serializers.Serializer):
        senderName = serializers.CharField(required=True, min_length=1, max_length=100)
        senderEmail = serializers.EmailField(required=True, min_length=10, max_length=150)
        message = serializers.CharField(required=True, min_length=10, max_length=500)
        responseToken = serializers.CharField(required=True, min_length=30)

        def validate_responseToken(self, value: str) -> str:
            validate = requests.post(
                url = 'https://hcaptcha.com/siteverify',
                data = { 'response': value, 'secret': CAPTCHA_SECRET },
                headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
            )

            if validate.status_code == 200:
                response = validate.json()
                if response.get('success'):
                    ts = datetime.strptime(response.get('challenge_ts', '2023-02-06T16:58:28.000000Z'), '%Y-%m-%dT%H:%M:%S.%fZ') + timedelta(seconds=300)
                    if ts < datetime.now() or response.get('hostname', '') not in ALLOWED_HOSTS:
                        raise serializers.ValidationError(detail='Validation Token invalid')
                else:
                    raise serializers.ValidationError(detail='Validation Token invalid')
            return value