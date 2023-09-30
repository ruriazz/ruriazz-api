from django.http import JsonResponse
from services import decorator
from rest_framework.request import Request
from utils.base.api_handler import BaseApiHandler
from utils.api import response
from . import validators
from . import services
from . import entities


class GuestHandler(BaseApiHandler):
    @staticmethod
    @decorator.authorized_form
    def post_subscribe(request: Request) -> JsonResponse:
        validation = validators.PostGuestSubscribeValidation(data=request.data)
        if not validation.is_valid(raise_exception=True):
            return response.SendJson(messages=validation._errors, status=response.Status.BAD_REQUEST)

        service = services.GuestSubscribe(entities.PostGuestSubscribeData(**validation.validated_data))
        if service.errors:
            return response.SendJson(messages=[str(i) for i in service.errors], status=response.Status.BAD_REQUEST)

        return response.SendJson(messages=["success to send message"], status=response.Status.HTTP_OK)