from django.core.handlers.wsgi import WSGIRequest
from libs.bases import BaseHandler

def page_not_found(request: WSGIRequest, *args, **kwarg):
    return BaseHandler.html_response(request=request, view='404.html', with_wrapper=False)