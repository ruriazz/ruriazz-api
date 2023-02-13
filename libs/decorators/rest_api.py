from rest_framework.decorators import api_view
from rest_framework.serializers import SerializerMetaclass
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
                try:
                    data = validator(data=instance._context.data)
                    meta_contract = 'E7001'
                    is_query_params = False
                except AttributeError:
                    data = validator(data=instance._context.query_params)
                    meta_contract = 'E7002'
                    is_query_params = True

                if not data.is_valid():
                    return APIResponse(message=data.errors, meta_contract=meta_contract)

                if is_query_params:
                    instance._context.query_params._mutable = True
                    instance._context.query_params.update(data.validated_data)
                    instance._context.query_params._mutable = False
                else:
                    instance._context.data.update(data.validated_data)

                func = f(instance)
                return func
            return wrapper
        self.func = decorate

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)