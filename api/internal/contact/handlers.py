from drf_yasg.utils import swagger_auto_schema
from libs.extensions import BaseApiHandler
from libs.decorators.rest_api import ApiMethod, DataValidation
from . import usecases
from . import serializers

class ContactApiHandler(BaseApiHandler):

    @swagger_auto_schema(method='post', auto_schema=None)
    @ApiMethod(['POST'])
    @DataValidation(serializers.Validator.PostSubmitContact)
    def submit_contact(self):
        usecase = usecases.ContactApiUsecase(context=self._context)
        if not usecase.submit_contact():
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)
        return self.response(self._context.data)