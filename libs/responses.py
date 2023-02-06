import re
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from configs.variables import API_META


class ApiResponse(JsonResponse):
    """API Response parser\n
    Attributes:
        - data:             any
        - message:          str | list | any
        - meta_contract:    str
        - pagination:       APIPagination
        - headers:          dictionary
    """
    class APIMeta:
        code: int
        http_code: int
        message: str

        def __init__(self, contract: str = 'S1001') -> None:
            meta = API_META.get(contract)
            if meta:
                self.code = int(re.sub('[^0-9]', '', contract))
                self.http_code = meta[0]
                self.message = meta[1]

        def _to_dict(self) -> dict:
            try: return {'code': self.code, 'httpCode': self.http_code, 'message': self.message}
            except: return {}

    class APIPagination:
        instance: any
        total_rows: int
        page: int
        limit: int
        total_page: int

        def __init__(self, instance: any, page: int, limit: int) -> None:
            self.instance = instance; self.page = page; self.limit = limit

        @property
        def paginated_data(self) -> any:
            paginator = Paginator(self.instance, self.limit)
            self.total_rows = paginator.count
            self.total_page = paginator.num_pages
            try:
                paginated_data = paginator.page(self.page).object_list
                return paginated_data
            except EmptyPage: return []

        def _to_dict(self) -> dict:
            return {
                'page': self.page,
                'limit': self.limit,
                'totalPage': self.total_page,
                'totalRows': self.total_rows
            }

    def __init__(self, data: any = None, message: any = None, meta_contract: str = 'S1000', pagination: APIPagination = None, headers: dict = {}, http_code: int = None) -> None:
        response_data = {}

        meta = self.APIMeta(contract=meta_contract)._to_dict()
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