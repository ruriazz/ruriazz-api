import os
from hooks.apps import APPS

app_config = {
    'applications': APPS,
    'debug': os.environ.get('DEBUG', '1') == '1',
    'secret_key': os.environ.get('SECRET_KEY', 'YOUR_SECRET_KEY'),
    'timezone': os.environ.get('TZ', 'UTC'),
    'allowed_hosts': os.environ.get('ALLOWED_HOSTS', 'localhost').split(','),
    'allowed_origins': os.environ.get('ALLOWED_ORIGINS', 'http://localhost').split(','),
    'contact_receipent': os.environ.get('COTACT_RECEIPENT', 'YOUR_COTACT_RECEIPENT').split(','),
    'email_host': os.environ.get('EMAIL_HOST', 'YOUR_EMAIL_HOST'),
    'email_port': int(os.environ.get('EMAIL_PORT', 'YOUR_EMAIL_PORT')),
    'email_host_user': os.environ.get('EMAIL_HOST_USER', 'YOUR_EMAIL_HOST_USER'),
    'email_host_password': os.environ.get('EMAIL_HOST_PASSWORD', 'YOUR_EMAIL_HOST_PASSWORD'),
    'email_use_tls': os.environ.get('EMAIL_USE_TLS', '1') == '1',
    'hcaptcha_sitekey': os.environ.get('HCAPTCHA_SITEKEY', 'YOUR_HCAPTCHA_SITEKEY'),
    'hcaptcha_secret': os.environ.get('HCAPTCHA_SECRET', 'YOUR_HCAPTCHA_SECRET'),
}