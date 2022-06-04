import threading, pytz
from django.core.handlers.wsgi import WSGIRequest

GLOBAL_REQUEST_STORAGE = threading.local()

class AppMidleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        GLOBAL_REQUEST_STORAGE.request = request
        response = self.get_response(request)
        return response

def get_client_timezone() -> str:
    from core.settings import TIME_ZONE
    try:
        tz = GLOBAL_REQUEST_STORAGE.request.headers.get('Time-Zone', 'nan')
        if tz in pytz.all_timezones:
            return tz

        return TIME_ZONE
    except AttributeError:
        return None
