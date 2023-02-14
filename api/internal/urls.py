from django.urls.conf import path

app_name = 'ruriazz_api'

from .contact.handlers import ContactApiHandler

urlpatterns = [
    path(r'contact', ContactApiHandler.submit_contact)
]