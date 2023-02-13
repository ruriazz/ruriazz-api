from django.core.handlers.wsgi import WSGIRequest
from corsheaders.signals import check_request_enabled


class OpenapiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        check_request_enabled.connect(self._is_cors_allowed)

    def __call__(self, request: WSGIRequest):
        response = self.get_response(request)
        return response

    @staticmethod
    def _is_cors_allowed(sender: any, request: WSGIRequest, **kwargs) -> bool:
        return {
            'True': OpenapiMiddleware._is_internal,
            'False': OpenapiMiddleware._is_openapi
        }[str(request.path.startswith('/internal'))](sender, request, **kwargs)

    def _is_openapi(sender: any, request: WSGIRequest, **kwargs) -> bool:
        return True

    def _is_internal(sender: any, request: WSGIRequest, **kwargs) -> bool:
        return False