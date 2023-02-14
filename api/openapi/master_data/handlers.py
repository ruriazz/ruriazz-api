from drf_yasg.utils import swagger_auto_schema
from libs.extensions import BaseApiHandler
from libs.decorators.rest_api import ApiMethod, DataValidation
from configs.openapi import Summary, Description
from .docs.response_schema import ResponseSchema
from .docs.param_schema import ParamSchema
from .usecases import MasterDataUsecase
from . import serializers


class MasterDataHandler(BaseApiHandler):

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2001, operation_description=Description.D2001, responses=ResponseSchema.idn_province_collections, manual_parameters=ParamSchema.idn_province_collections, operation_id='openapi-12001')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnProvinceCollection)
    def idn_province_collections(self):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_province_collections
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnProvinceCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2002, operation_description=Description.D2002, responses=ResponseSchema.idn_district_collections, manual_parameters=ParamSchema.idn_district_collections, operation_id='openapi-12002')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnDistrictCollection)
    def idn_district_collections(self):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_district_collections()
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnDistrictCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2003, operation_description=Description.D2003, responses=ResponseSchema.idn_district_collection_by_province, manual_parameters=ParamSchema.idn_district_collection_by_province, operation_id='openapi-12003')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnDistrictCollection)
    def idn_district_collection_by_province(self, province_slug: str = None):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_district_collections(province_slug)
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnDistrictCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2004, operation_description=Description.D2004, responses=ResponseSchema.idn_subdistrict_collections, manual_parameters=ParamSchema.idn_subdistrict_collections, operation_id='openapi-12004')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnSubdistrictCollection)
    def idn_subdistrict_collections(self):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_subdistrict_collections()
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnSubdistrictCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2005, operation_description=Description.D2005, responses=ResponseSchema.idn_subdistrict_collection_by_district, manual_parameters=ParamSchema.idn_subdistrict_collection_by_district, operation_id='openapi-12005')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnSubdistrictCollection)
    def idn_subdistrict_collection_by_district(self, district_slug: str = None):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_subdistrict_collections(district_slug=district_slug)
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnSubdistrictCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2006, operation_description=Description.D2006, responses=ResponseSchema.idn_urban_village_collections, manual_parameters=ParamSchema.idn_urban_village_collections, operation_id='openapi-12006')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnUrbanVillageCollection)
    def idn_urban_village_collections(self):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_urban_village_collections()
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnUrbanVillageCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2007, operation_description=Description.D2007, responses=ResponseSchema.idn_urban_village_collection_by_subdistrict, manual_parameters=ParamSchema.idn_urban_village_collection_by_subdistrict, operation_id='openapi-12007')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnUrbanVillageCollection)
    def idn_urban_village_collection_by_subdistrict(self, subdistrict_slug: str = None):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_urban_village_collections(subdistrict_slug=subdistrict_slug)
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnUrbanVillageCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2008, operation_description=Description.D2008, responses=ResponseSchema.idn_subdistrict_collection_by_province, manual_parameters=ParamSchema.idn_subdistrict_collection_by_province, operation_id='openapi-12008')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnSubdistrictCollection)
    def idn_subdistrict_collection_by_province(self, province_slug: str = None):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_subdistrict_collections(province_slug=province_slug)
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnSubdistrictCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results.data, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2009, operation_description=Description.D2009, responses=ResponseSchema.idn_urban_village_collection_by_district, manual_parameters=ParamSchema.idn_urban_village_collection_by_district, operation_id='openapi-21009')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnUrbanVillageCollection)
    def idn_urban_village_collection_by_district(self, district_slug: str = None):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_urban_village_collections(district_slug=district_slug)
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnUrbanVillageCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results, pagination=pagination)

    @swagger_auto_schema(tags=['Master Data'], method='get', operation_summary=Summary.S2010, operation_description=Description.D2010, responses=ResponseSchema.idn_urban_village_collection_by_province, manual_parameters=ParamSchema.idn_urban_village_collection_by_province, operation_id='openapi-22010')
    @ApiMethod(['GET'])
    @DataValidation(serializers.Validators.GetIdnUrbanVillageCollection)
    def idn_urban_village_collection_by_province(self, province_slug: str = None):
        usecase = MasterDataUsecase(context=self._context)
        collections = usecase.idn_urban_village_collections(province_slug=province_slug)
        if collections is None:
            return self.response(message=usecase.errors, meta_contract=usecase.meta_response)

        pagination = self.paginate_data(instance=collections)
        results = serializers.IdnUrbanVillageCollectionSerializer(instance=pagination.paginated_data, many=True)
        return self.response(data=results, pagination=pagination)