from rest_framework.request import Request
from utils.api import response
from utils.helpers.hcaptcha import token_validation


def authorized_form(function):
    def wrapper(request: Request, *args, **kwargs):
        submit_token = request.headers.get('X-Submit-Token')
        if not submit_token:
            return response.SendJson(status=response.Status.BAD_REQUEST, messages=['unauthorized data'])

        if not token_validation(submit_token):
            return response.SendJson(status=response.Status.BAD_REQUEST, messages=['unauthorized data'])

        func = function(request, *args, **kwargs)
        return func
    return wrapper