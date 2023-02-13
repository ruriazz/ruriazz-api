from drf_yasg.utils import swagger_auto_schema
from libs.extensions import BaseApiHandler
from libs.decorators.rest_api import ApiMethod
from configs.openapi import Summary, Description
from .response_schema import ResponseSchema


class MasterDataHandler(BaseApiHandler):

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2001, operation_description=Description.D2001, responses=ResponseSchema.idn_province_collections, operation_id='openapi-12001')
    @ApiMethod(['GET'])
    def idn_province_collections(self):
        return self.response()

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2002, operation_description=Description.D2002, responses=ResponseSchema.idn_province_collections, operation_id='openapi-12002')
    @ApiMethod(['GET'])
    def idn_district_collections(self):
        return self.response()

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2003, operation_description=Description.D2003, responses=ResponseSchema.idn_province_collections, operation_id='openapi-12003')
    @ApiMethod(['GET'])
    def idn_district_collection_by_province(self, province_slug: str = None):
        return self.response()

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2004, operation_description=Description.D2004, responses=ResponseSchema.idn_province_collections, operation_id='openapi-12004')
    @ApiMethod(['GET'])
    def idn_subdistrict_collections(self):
        return self.response()

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2005, operation_description=Description.D2005, responses=ResponseSchema.idn_province_collections, operation_id='openapi-12005')
    @ApiMethod(['GET'])
    def idn_subdistrict_collection_by_district(self, district_slug: str = None):
        return self.response()

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2006, operation_description=Description.D2006, responses=ResponseSchema.idn_province_collections, operation_id='openapi-12006')
    @ApiMethod(['GET'])
    def idn_urban_village_collections(self):
        return self.response()

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2007, operation_description=Description.D2007, responses=ResponseSchema.idn_province_collections, operation_id='openapi-21007')
    @ApiMethod(['GET'])
    def idn_urban_village_collection_by_subdistrict(self, subdistrict_slug: str = None):
        return self.response()