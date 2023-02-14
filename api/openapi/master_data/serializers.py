from email.policy import default
from libs.extensions import serializers, BaseQueryParameter
from models.idn_province.models import IdnProvince
from models.idn_district.models import IdnDistrict
from models.idn_subdistrict.models import IdnSubdistrict
from models.idn_urban_village.models import IdnUrbanVillage


class IdnProvinceCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdnProvince
        fields = ['code', 'slug', 'isoCode', 'name']

class IdnDistrictCollectionSerializer(serializers.ModelSerializer):
    provinceName = serializers.CharField(source='idnProvince.name')
    class Meta:
        model = IdnDistrict
        fields = ['code', 'slug', 'provinceName', 'datiName', 'name', 'alias']

class IdnSubdistrictCollectionSerializer(serializers.ModelSerializer):
    provinceName = serializers.CharField(source='idnProvince.name')
    districtName = serializers.SerializerMethodField()
    class Meta:
        model = IdnSubdistrict
        fields = ['code', 'slug', 'provinceName', 'districtName', 'name', 'alias']

    def get_districtName(self, obj) -> str:
        return f"{obj.idnDistrict.datiName} {obj.idnDistrict.name}"

class IdnUrbanVillageCollectionSerializer(serializers.Serializer):
    code = serializers.CharField()
    slug = serializers.CharField()
    provinceName = serializers.CharField(source='idnProvince.name')
    districtName = serializers.SerializerMethodField()
    subdistrictName = serializers.CharField(source='idnSubdistrict.name')
    name = serializers.CharField()
    alias = serializers.CharField()
    postalCode = serializers.CharField()
    class Meta:
        model = IdnUrbanVillage
        fields = ['code', 'slug', 'provinceName', 'districtName', 'subdistrictName', 'name', 'alias', 'postalCode']

    def get_districtName(self, obj) -> str:
        return f"{obj.idnDistrict.datiName} {obj.idnDistrict.name}"

class Validators:
    class GetIdnProvinceCollection(BaseQueryParameter):
        pass

    class GetIdnDistrictCollection(BaseQueryParameter):
        pass

    class GetIdnSubdistrictCollection(BaseQueryParameter):
        pass

    class GetIdnUrbanVillageCollection(BaseQueryParameter):
        pass