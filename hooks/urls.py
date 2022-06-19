from django.urls import path

from .mailer.views import MailerView
from .oauth.views import OAuthView

app_name = "webhooks"

urlpatterns = [
    path('mail', MailerView.main),
    path('oauth', OAuthView.main)
]
