from django.urls import path
from api.warkopwarawiri.guest.handlers import GuestHandler


app_name = 'warkopwarawiri-api'

urlpatterns = [
    path(r'guest/subscribe', GuestHandler.as_view({'post': 'post_subscribe'}))
]