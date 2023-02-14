from libs.extensions import BaseModel, models
from models.idn_district.models import IdnDistrict
from models.idn_province.models import IdnProvince

# Create your models here.
class IdnSubdistrict(BaseModel):
    id = models.SmallAutoField(primary_key=True)
    idnDistrict = models.ForeignKey(to=IdnDistrict, on_delete=models.CASCADE, db_column='idnDistrictId', related_name='subdistricts')
    idnProvince = models.ForeignKey(to=IdnProvince, on_delete=models.CASCADE, db_column='idnProvinceId', related_name='subdistricts')
    slug = models.SlugField(max_length=75, unique=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=75)
    alias = models.CharField(max_length=75, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(default=None, null=True)

    class Meta:
        db_table = 'md_idn_subdistrict'