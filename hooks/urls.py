from django.urls import path

from .mailer.views import MailerView

app_name = "webhooks"

urlpatterns = [
    path('mail', MailerView.main)
]
