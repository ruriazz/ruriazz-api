from drf_yasg.utils import swagger_auto_schema
from libs.extensions import BaseApiHandler
from libs.decorators.rest_api import ApiMethod
from configs.openapi import Summary, Description
from .docs.response_schema import ResponseSchema

class ShortUrlHandler(BaseApiHandler):
    @swagger_auto_schema(tags=['URL Shortner'], method='post', operation_summary=Summary.S3001, operation_description=Description.D3001, operation_id='openapi-13001')
    @ApiMethod(['POST'])
    def collections(self):
        return self.response()
