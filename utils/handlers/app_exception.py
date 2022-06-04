from http.client import METHOD_NOT_ALLOWED
from rest_framework.views import exception_handler
from utils.api_response import ApiResponse

def app_exception(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if METHOD_NOT_ALLOWED == response.status_code:
            response.status_code = METHOD_NOT_ALLOWED
            
        response = ApiResponse(data=response.data.get("detail"), status=response.status_code)

    return response