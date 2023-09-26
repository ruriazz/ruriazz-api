from django.http import JsonResponse
from rest_framework.request import Request
from utils.base.api_handler import BaseApiHandler
from utils.api import response


class RootHandler(BaseApiHandler):
    @staticmethod
    def default(_: Request) -> JsonResponse:
        return response.SendJson(messages=["fly in the sky!"], status=response.Status.HTTP_OK)