from django.http import JsonResponse
from .meta import APIMeta
from .pagination import APIPagination


class APIResponse(JsonResponse):
    """API Response parser\n
    Attributes:
        - data:             any
        - message:          str | list | any
        - meta_contract:    str
        - pagination:       APIPagination
        - headers:          dictionary
    """

    def __init__(self, data: any = None, message: any = None, meta_contract: str = 'S1000', pagination: APIPagination = None, headers: dict = {}, http_code: int = None) -> None:
        response_data = {}

        meta = APIMeta(contract=meta_contract)._to_dict()
        if meta: response_data['meta'] = meta

        if data is not None:
            if isinstance(data, str):
                response_data['meta']['message'] = data
            else:
                try: response_data['data'] = data.data
                except: response_data['data'] = data
        elif message is not None:
            response_data['message'] = message

        if pagination:
            response_data['pagination'] = pagination._to_dict()

        if http_code:
            response_data['meta']['httpCode'] = http_code

        super().__init__(data=response_data, status=response_data['meta']['httpCode'], headers=headers)