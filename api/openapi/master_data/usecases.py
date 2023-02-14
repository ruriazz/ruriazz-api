from django.db.models import Q, ExpressionWrapper, BooleanField, QuerySet
from libs.extensions import BaseApiUsecase
from models.idn_province.models import IdnProvince
from models.idn_district.models import IdnDistrict
from models.idn_subdistrict.models import IdnSubdistrict
from models.idn_urban_village.models import IdnUrbanVillage


class MasterDataUsecase(BaseApiUsecase):
    @property
    def idn_province_collections(self) -> QuerySet[IdnProvince]:
        try:
            query = self._context.query_params.get('query')
            if query:
                return IdnProvince.objects.filter(name__icontains=query) \
                    .annotate(is_match_order=ExpressionWrapper(Q(name__istartswith=query), output_field=BooleanField())) \
                    .order_by('-is_match_order')

            return IdnProvince.objects.all().order_by('name')
        except Exception as err:
            self.errors = str(err)
            self.meta_response = 'E7008'

    def idn_district_collections(self, province_slug: str = None) -> QuerySet[IdnDistrict]:
        try:
            if province_slug:
                province = IdnProvince.objects.only('id').get(slug=province_slug)
                collections = IdnDistrict.objects.filter(idnProvince_id=province.id)
            else:
                collections = IdnDistrict.objects.all()

            query = self._context.query_params.get('query')
            if query:
                return collections.filter(Q(name__icontains=query) | Q(alias__icontains=query)) \
                    .annotate(is_match_order=ExpressionWrapper(Q(name__istartswith=query), output_field=BooleanField())) \
                    .order_by('-is_match_order', 'name')

            return collections.order_by('name', 'code')
        except Exception as err:
            if isinstance(err, IdnProvince.DoesNotExist):
                self.errors = f"No Indonesian Province found with slug '{province_slug}'"
                self.meta_response = 'E7011'
            else:
                self.errors = str(err)
                self.meta_response = 'E7008'

    def idn_subdistrict_collections(self, district_slug: str = None, province_slug: str = None) -> QuerySet[IdnSubdistrict]:
        try:
            if district_slug:
                district = IdnDistrict.objects.only('id').get(slug=district_slug)
                collections = IdnSubdistrict.objects.filter(idnDistrict_id=district.id)
            elif province_slug:
                province = IdnProvince.objects.only('id').get(slug=province_slug)
                collections = IdnSubdistrict.objects.filter(idnProvince_id=province.id)
            else:
                collections = IdnSubdistrict.objects.all()

            query = self._context.query_params.get('query')
            if query:
                return collections.filter(Q(name__icontains=query) | Q(alias__icontains=query)) \
                    .annotate(is_match_order=ExpressionWrapper(Q(name__istartswith=query), output_field=BooleanField())) \
                    .order_by('-is_match_order', 'name')

            return collections.order_by('name', 'code')
        except Exception as err:
            if isinstance(err, IdnDistrict.DoesNotExist):
                self.errors = f"No Indonesian District found with slug '{district_slug}'"
                self.meta_response = 'E7011'
            elif isinstance(err, IdnProvince.DoesNotExist):
                self.errors = f"No Indonesian Province found with slug '{province_slug}'"
                self.meta_response = 'E7011'
            else:
                self.errors = str(err)
                self.meta_response = 'E7008'

    def idn_urban_village_collections(self, subdistrict_slug: str = None, district_slug: str = None, province_slug: str = None) -> QuerySet[IdnUrbanVillage]:
        try:
            if subdistrict_slug:
                subdistrict = IdnSubdistrict.objects.only('id').get(slug=subdistrict_slug)
                collections = IdnUrbanVillage.objects.filter(idnSubdistrict_id=subdistrict.id)
            elif district_slug:
                district = IdnDistrict.objects.only('id').get(slug=district_slug)
                collections = IdnUrbanVillage.objects.filter(idnDistrict_id=district.id)
            elif province_slug:
                province = IdnProvince.objects.only('id').get(slug=province_slug)
                collections = IdnUrbanVillage.objects.filter(idnProvince_id=province.id)
            else:
                collections = IdnUrbanVillage.objects.all()

            query = self._context.query_params.get('query')
            if query:
                return collections.filter(Q(name__icontains=query) | Q(alias__icontains=query)) \
                    .annotate(is_match_order=ExpressionWrapper(Q(name__istartswith=query), output_field=BooleanField())) \
                    .order_by('-is_match_order', 'name')

            return collections.order_by('name', 'code')
        except Exception as err:
            if isinstance(err, IdnSubdistrict.DoesNotExist):
                self.errors = f"No Indonesian Subdistrict found with slug '{subdistrict_slug}'"
                self.meta_response = 'E7011'
            elif isinstance(err, IdnDistrict.DoesNotExist):
                self.errors = f"No Indonesian District found with slug '{district_slug}'"
                self.meta_response = 'E7011'
            elif isinstance(err, IdnProvince.DoesNotExist):
                self.errors = f"No Indonesian Province found with slug '{province_slug}'"
                self.meta_response = 'E7011'
            else:
                self.errors = str(err)
                self.meta_response = 'E7008'