from rest_framework.decorators import api_view
from rest_framework.serializers import SerializerMetaclass
from rest_framework.request import Request
from libs.extensions import BaseApiHandler
from libs.response import APIResponse

class ApiMethod:
    def __init__(self, http_method_names: list = ['GET'], authenticated: bool = False, valid_acl: bool = False):
        def decorate(f):
            @api_view(http_method_names)
            def wrapper(context, *args, **kwargs):
                func = f(BaseApiHandler(context=context), *args, **kwargs)
                return func
            return wrapper
        self.func = decorate

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class DataValidation:
    def __init__(self, validator: SerializerMetaclass) -> None:
        def decorate(f):
            def wrapper(instance, *args, **kwargs):
                validatation = self._get_validator(context=instance._context)
                err, meta, instance._context = validatation(validator, instance._context)
                if err:
                    return APIResponse(message=err, meta_contract=meta)

                func = f(instance, *args, **kwargs)
                return func
            return wrapper
        self.func = decorate

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def _get_validator(self, context: Request):
        if str(context.method).lower() in ['get', 'delete']:
            return self._validate_query_params

        return self._validate_data

    def _validate_data(self, validator: SerializerMetaclass, context: Request) -> tuple:
        _serializer = validator(data=context.data)
        if not _serializer.is_valid():
            return _serializer.errors, 'E7002', context

        context.data.update(_serializer.validated_data)
        return None, None, context

    def _validate_query_params(self, validator: SerializerMetaclass, context: Request) -> tuple:
        _serializer = validator(data=context.query_params)
        if not _serializer.is_valid():
            return _serializer.errors, 'E7001', context

        context.query_params._mutable = True
        context.query_params.update(_serializer.validated_data)
        context.query_params._mutable = False
        return None, None, context