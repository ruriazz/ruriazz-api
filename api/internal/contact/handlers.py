from libs.bases import BaseApiHandler
from rest_framework.request import Request
from . import usecases
from . import serializers

class ContactApiHandler(BaseApiHandler):

    @staticmethod
    @BaseApiHandler.api_view(['POST'])
    def submit_contact(request: Request):
        post_data = serializers.Validator.PostSubmitContact(data=request.data)
        if not post_data.is_valid():
            return BaseApiHandler.ApiResponse(message=post_data.errors, meta_contract='E7001')

        request.data.update(post_data.validated_data)
        usecase = usecases.ContactApiUsecase(context=request)
        if not usecase.submit_contact():
            return BaseApiHandler.ApiResponse(message=usecase.errors, meta_contract=usecase.meta_response)
        return BaseApiHandler.ApiResponse(request.data)