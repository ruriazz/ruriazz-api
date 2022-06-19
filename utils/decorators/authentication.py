import base64
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from core.app_config import app_config

class BasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass

def is_developer(function):
    def wrapper(request, *args, **kwargs):
        auth = request.META.get('HTTP_AUTHORIZATION', 'undefined').split()

        if not auth or auth[0].lower() != "basic":
            raise exceptions.AuthenticationFailed("Invalid basic header. No credentials provided.")

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed("Invalid basic header. No credentials provided.")
        if len(auth) > 2:
            raise exceptions.AuthenticationFailed("Invalid basic header. Credential string is not properly formatted.")

        try:
            auth_decoded = base64.b64decode(auth[1]).decode("utf-8")
            auth_decoded.split(":")
        except (UnicodeDecodeError, ValueError):
            raise exceptions.AuthenticationFailed("Invalid basic header. Credentials not correctly encoded.")

        if auth_decoded not in app_config.get('developer_auth'):
            raise exceptions.AuthenticationFailed('Invalid basic header. Credentials not registered.')

        func = function(request, *args, **kwargs)
        
        return func

    return wrapper