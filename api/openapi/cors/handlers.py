from drf_yasg.utils import swagger_auto_schema
from libs.extensions import BaseApiHandler
from libs.decorators.rest_api import ApiMethod
from configs.openapi import Summary, Description


class CorsHandler(BaseApiHandler):
    @swagger_auto_schema(tags=['CORS'], method='post', operation_summary=Summary.S1001, operation_description=Description.D1001, operation_id='openapi-11001')
    @ApiMethod(['POST'])
    def collections(self):
        return self.response()