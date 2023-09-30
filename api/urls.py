from django.urls import include, path

from . import RootHandler
from api.personal.handlers import PersonalHandler


urlpatterns = [
    path('', RootHandler.as_view({'get': 'default'})),

    # Prefix: /personal
    path(r'personal/contact', PersonalHandler.as_view({'post': 'post_contact'})),

    # Prefix: /warkopwarawiri
    path(r'warkopwarawiri/', include('api.warkopwarawiri.urls', namespace='warkopwarawiri-api'))
]