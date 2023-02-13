from inflection import camelize
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema


class CamelCaseOperationIDAutoSchema(SwaggerAutoSchema):
   def get_operation_id(self, operation_keys):
      operation_id = super(CamelCaseOperationIDAutoSchema, self).get_operation_id(operation_keys)
      return camelize(operation_id, uppercase_first_letter=False)


class Summary:
    S1001 = 'Registration'
    S1002 = ''
    S1003 = ''

    S2001 = 'IDN Province'
    S2002 = 'IDN District/Regency'
    S2003 = S2002
    S2004 = 'IDN Sub-district'
    S2005 = S2004
    S2006 = 'IDN Urban Village'
    S2007 = S2006

    S3001 = 'Create Short URL'

class Description:
    D1001 = 'Cross-Origin Resource Sharing (CORS) Host Registration'
    D1002 = ''
    D1003 = ''

    D2001 = 'Indonesian Province Collections'
    D2002 = 'Indonesian Disctrict/Regency Collections'
    D2003 = 'Indonesian District/Regency Collection with Province slug'
    D2004 = 'Indonesian Sub-district Collections'
    D2005 = 'Indonesian Sub-district Collection with District slug'
    D2006 = 'Indonesian Urban Village Collections'
    D2007 = 'Indonesian Urban Village Collection with Sub-district slug'

    D3001 = 'Generate New Short URL'


info = openapi.Info(title="ruriazz - OpenAPI", default_version='v1', description="")
schema = get_schema_view(info=info, public=True)