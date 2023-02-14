from django.db.models import Q, ExpressionWrapper, BooleanField, QuerySet
from libs.extensions import BaseApiUsecase
from models.idn_province.models import IdnProvince
from models.idn_district.models import IdnDistrict


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
                    .order_by('-is_match_order')

            return collections.order_by('name', 'code')
        except Exception as err:
            if isinstance(err, IdnProvince.DoesNotExist):
                self.errors = f"No Indonesian Province found with slug '{province_slug}'"
                self.meta_response = 'E7011'
            else:
                self.errors = str(err)
                self.meta_response = 'E7008'