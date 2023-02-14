from drf_yasg import openapi

class ParamSchema:
    gmap_link_info = [
        openapi.Parameter(name='url', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING, default=None, description='Google Maps link value'),
    ]