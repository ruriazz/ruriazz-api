from drf_yasg import openapi

class ParamSchema:
    idn_province_collections = [
        openapi.Parameter(name='query', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING, default=None, description='Search query based on name'),
        openapi.Parameter(name='limit', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_INTEGER, default=100, description='Pagination limit number. [min=1, max=1000]'),
        openapi.Parameter(name='page', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_INTEGER, default=1, description='Pagination page number. [min=1]')
    ]

    idn_district_collections = [
        openapi.Parameter(name='query', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING, default=None, description='Search query based on name'),
        openapi.Parameter(name='limit', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_INTEGER, default=100, description='Pagination limit number. [min=1, max=1000]'),
        openapi.Parameter(name='page', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_INTEGER, default=1, description='Pagination page number. [min=1]')
    ]

    idn_district_collection_by_province = [
        openapi.Parameter(name='query', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING, default=None, description='Search query based on name'),
        openapi.Parameter(name='limit', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_INTEGER, default=100, description='Pagination limit number. [min=1, max=1000]'),
        openapi.Parameter(name='page', in_=openapi.IN_QUERY, required=False, type=openapi.TYPE_INTEGER, default=1, description='Pagination page number. [min=1]')
    ]