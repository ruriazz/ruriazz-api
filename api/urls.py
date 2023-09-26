from django.urls import path

from . import RootHandler
from api.personal.handlers import PersonalHandler


urlpatterns = [
    path('', RootHandler.as_view({'get': 'default'})),

    # Prefix: /personal
    path(r'personal/contact', PersonalHandler.as_view({'post': 'post_contact'}))
]