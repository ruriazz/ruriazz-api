from django.urls.conf import path, re_path, include

app_name = 'openapi'


from .cors.handlers import CorsHandler
from .short_url.handlers import ShortUrlHandler
from .master_data.handlers import MasterDataHandler
from .google_place.handlers import GooglePlaceHandler



urlpatterns = [
    re_path(
        r'^v1/', include([
            # CORS
            path(r'cors', CorsHandler.collections),

            # Short URL
            path(r'short-url', ShortUrlHandler.collections),

            # Master Data
            path(r'md/idn-province', MasterDataHandler.idn_province_collections),
            path(r'md/idn-province/<slug:province_slug>/district', MasterDataHandler.idn_district_collection_by_province),
            path(r'md/idn-province/<slug:province_slug>/subdistrict', MasterDataHandler.idn_subdistrict_collection_by_province),
            path(r'md/idn-province/<slug:province_slug>/urban-village', MasterDataHandler.idn_urban_village_collection_by_province),
            path(r'md/idn-district', MasterDataHandler.idn_district_collections),
            path(r'md/idn-district/<slug:district_slug>/subdistrict', MasterDataHandler.idn_subdistrict_collection_by_district),
            path(r'md/idn-district/<slug:district_slug>/urban-village', MasterDataHandler.idn_urban_village_collection_by_district),
            path(r'md/idn-subdistrict', MasterDataHandler.idn_subdistrict_collections),
            path(r'md/idn-subdistrict/<slug:subdistrict_slug>/urban-village', MasterDataHandler.idn_urban_village_collection_by_subdistrict),
            path(r'md/idn-urban-village', MasterDataHandler.idn_urban_village_collections),

            # Google Place
            path(r'google-place', GooglePlaceHandler.gmap_link_info)
        ]),
    )
]