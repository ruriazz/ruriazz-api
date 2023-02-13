import os
from urllib import request
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from libs.response import APIResponse
from configs.settings import BASE_DIR
from rest_framework.generics import GenericAPIView


class BaseHandler:
    @staticmethod
    def html_response(request: WSGIRequest, view: str, context: dict = {}, page_title: str = None, with_wrapper: bool = True) -> response.HttpResponse:
        if not view.endswith('.html'):
            view = f"{view}.html"

        menu_index = ['index.html', 'resume.html', 'portfolio.html', 'contact.html']; active_menu = []
        for menu in menu_index:
            val = ''
            if view == menu: val = 'active'
            active_menu.append(val)

        context['page_content'] = view
        context['page_properties'] = {
            'active_menu': active_menu,
            'title': page_title or 'ruriazz'
        }

        if with_wrapper:
            return render(request, 'templates/wrapper.html', context=context)

        return render(request, view)

    @staticmethod
    def file_response(file_path: str, content_type: str) -> response.HttpResponse:
        with open(os.path.join(BASE_DIR, file_path), 'r') as f:
            return HttpResponse(f.read(), content_type=content_type)

class BaseApiHandler(GenericAPIView):
    _context: Request
    _args: tuple

    def __init__(self, context: Request, *args, **kwargs) -> None:
        self._context = context
        self._args = args
        for key in kwargs.keys(): setattr(self, key, kwargs[key])

    def response(self, data: any = None, message: any = None, meta_contract: str = 'S1000', headers: dict = {}) -> Response:
        return APIResponse(data=data, message=message, meta_contract=meta_contract, headers=headers)

    def paginate_data(self):
        pass

class BaseApiUsecase:
    _context: Request

    errors: any
    meta_response: str = 'S1000'

    def __init__(self, context: request = None) -> None:
        self._context = context
