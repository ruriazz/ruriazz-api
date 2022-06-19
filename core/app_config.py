import os
from hooks.apps import APPS

app_config = {
    'applications': APPS,
    'debug': os.environ.get('DEBUG', '1') == '1',
    'secret_key': os.environ.get('SECRET_KEY', 'YOUR_SECRET_KEY'),
    'timezone': os.environ.get('TZ', 'UTC'),
    'allowed_hosts': os.environ.get('ALLOWED_HOSTS', 'localhost').split(','),
    'allowed_origins': os.environ.get('ALLOWED_ORIGINS', 'http://localhost').split(','),
    'contact_receipent': os.environ.get('COTACT_RECEIPENT', 'YOUR_COTACT_RECEIPENT'),
    'contact_reply_to': os.environ.get('CONTACT_REPLY_TO', 'YOUR_CONTACT_REPLY_TO'),
    'contact_name': os.environ.get('CONTACT_NAME', 'YOUR_CONTACT_NAME'),
    'email_host': os.environ.get('EMAIL_HOST', 'YOUR_EMAIL_HOST'),
    'email_port': int(os.environ.get('EMAIL_PORT', 'YOUR_EMAIL_PORT')),
    'email_host_user': os.environ.get('EMAIL_HOST_USER', 'YOUR_EMAIL_HOST_USER'),
    'email_host_password': os.environ.get('EMAIL_HOST_PASSWORD', 'YOUR_EMAIL_HOST_PASSWORD'),
    'email_use_tls': os.environ.get('EMAIL_USE_TLS', '1') == '1',
    'hcaptcha_sitekey': os.environ.get('HCAPTCHA_SITEKEY', 'YOUR_HCAPTCHA_SITEKEY'),
    'hcaptcha_secret': os.environ.get('HCAPTCHA_SECRET', 'YOUR_HCAPTCHA_SECRET'),
    'sib_api_url': os.environ.get('SIB_API_URL', 'https://api.sendinblue.com/v3'),
    'sib_key': os.environ.get('SIB_KEY', 'YOUR_SIB_KEY'),
    'developer_auth': os.environ.get('DEVELOPER_AUTH', 'YOUR_DEVELOPER_AUTH').split(',')
}