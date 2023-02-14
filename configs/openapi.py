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
    S2002 = 'IDN District/Regency [1]'
    S2003 = 'IDN District/Regency [2]'
    S2004 = 'IDN Sub-district [3]'
    S2005 = 'IDN Sub-district [1]'
    S2006 = 'IDN Urban Village [4]'
    S2007 = 'IDN Urban Village [3]'
    S2008 = 'IDN Sub-district [2]'
    S2009 = 'IDN Urban Village [1]'
    S2010 = 'IDN Urban Village [2]'

    S3001 = 'Create Short URL'

    S4001 = 'GooleMaps link'

class Description:
    D1001 = 'Cross-Origin Resource Sharing (CORS) Host Registration'
    D1002 = ''
    D1003 = ''

    D2001 = 'Indonesian Province Collections'
    D2002 = 'Indonesian Disctrict/Regency Collections'
    D2003 = 'Indonesian District/Regency Collection by Province slug'
    D2004 = 'Indonesian Sub-district Collections'
    D2005 = 'Indonesian Sub-district Collection by District slug'
    D2006 = 'Indonesian Urban Village Collections'
    D2007 = 'Indonesian Urban Village Collection by Sub-district slug'
    D2008 = 'Indonesian Sub-district Collection by Province slug'
    D2009 = 'Indonesian Urban Village Collection by District slug'
    D2010 = 'Indonesian Urban Village Collection by Province slug'

    D3001 = 'Generate New Short URL'

    D4001 = 'Get Place info from GoogleMaps link'


info = openapi.Info(title="ruriazz - OpenAPI", default_version='v1', description="")
schema = get_schema_view(info=info, public=True)