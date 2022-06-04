from django.urls.exceptions import Resolver404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .api_response import ApiResponse
from http.client import NOT_FOUND, INTERNAL_SERVER_ERROR

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'])
def page_not_found(request: Request, exception: Resolver404) -> Response:
    return ApiResponse(data='Endpoint not found.', status=NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'])
def server_error(request: Request) -> Response:
    return ApiResponse(data='Internal server error.', status=INTERNAL_SERVER_ERROR)