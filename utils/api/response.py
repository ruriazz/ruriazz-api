from http import HTTPStatus
from typing import Any, Dict, List, Union
from django.http import JsonResponse


class Status:
    HTTP_OK = HTTPStatus.OK
    BAD_REQUEST = HTTPStatus.BAD_REQUEST

def SendJson(data: Any = None, messages: Union[List[str], Dict, List[Dict], str] = None, status: Status = Status.HTTP_OK) -> JsonResponse:
    response = {'success': status >= HTTPStatus.OK and status < HTTPStatus.BAD_REQUEST, 'status': status, 'messages': messages, 'data': data}

    sanitized_response = {}
    for key in response.keys():
        if not isinstance(response[key], bool) and not response[key]:
            continue
        sanitized_response[key] = response[key]

    return JsonResponse(data=sanitized_response, status=status)
