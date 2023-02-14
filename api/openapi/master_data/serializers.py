from email.policy import default
from libs.extensions import serializers, BaseQueryParameter
from models.idn_province.models import IdnProvince
from models.idn_district.models import IdnDistrict


class IdnProvinceCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdnProvince
        fields = ['code', 'slug', 'isoCode', 'name']

class IdnDistrictCollectionSerializer(serializers.ModelSerializer):
    provinceName = serializers.CharField(source='idnProvince.name')
    class Meta:
        model = IdnDistrict
        fields = ['code', 'slug', 'provinceName', 'datiName', 'name', 'alias']

class Validators:
    class GetIdnProvinceCollection(BaseQueryParameter):
        pass

    class GetIdnDistrictCollection(BaseQueryParameter):
        pass