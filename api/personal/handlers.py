from django.http import JsonResponse
from rest_framework.request import Request
from utils.base.api_handler import BaseApiHandler
from utils.api import response
from services import decorator
from . import validators
from . import entities
from . import services


class PersonalHandler(BaseApiHandler):
    @staticmethod
    @decorator.authorized_form
    def post_contact(request: Request) -> JsonResponse:
        validation = validators.PostContactJsonValidation(data=request.data)
        if not validation.is_valid(raise_exception=True):
            return response.SendJson(messages=validation._errors, status=response.Status.BAD_REQUEST)

        usecase = services.PersonalContact(entities.PostContactData(**validation.validated_data))
        if usecase.errors:
            return response.SendJson(messages=[str(i) for i in usecase.errors], status=response.Status.BAD_REQUEST)

        return response.SendJson(messages=["success to send message"], status=response.Status.HTTP_OK)