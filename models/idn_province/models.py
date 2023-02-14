from libs.extensions import BaseModel, models

# Create your models here.
class IdnProvince(BaseModel):
    id = models.SmallAutoField(primary_key=True)
    slug = models.SlugField(max_length=75, unique=True)
    code = models.CharField(max_length=5, unique=True)
    isoCode = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=75)
    geographicArea = models.CharField(max_length=75)
    capital = models.CharField(max_length=75, null=True)
    image = models.CharField(max_length=255, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(default=None, null=True)

    class Meta:
        db_table = 'md_idn_province'