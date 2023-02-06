from django.urls import re_path, include

urlpatterns = [
    re_path(r'', include('web.urls', namespace='ruriazz_web')),
    re_path(r'^internal/', include('api.internal.urls', namespace='internal_api')),
    re_path(r'^openapi/', include('api.openapi.urls', namespace='openapi')),
]

handler404 = 'web.property.handlers.page_not_found'
handler500 = 'web.property.handlers.page_not_found'
handler403 = 'web.property.handlers.page_not_found'
handler400 = 'web.property.handlers.page_not_found'