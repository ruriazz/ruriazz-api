from drf_yasg.utils import swagger_auto_schema
from libs.extensions import BaseApiHandler
from libs.decorators.rest_api import ApiMethod, DataValidation
from configs.openapi import Summary, Description
from .docs.param_schema import ParamSchema
from .docs.response_shema import ResponseSchema


class GooglePlaceHandler(BaseApiHandler):

    @swagger_auto_schema(tags=['Google Place'], method='get', operation_summary=Summary.S4001, operation_description=Description.D4001, operation_id='openapi-14001')
    @ApiMethod(['GET'])
    def gmap_link_info(self):
        pass