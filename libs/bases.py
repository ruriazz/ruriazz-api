import os
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework import decorators
from rest_framework.request import Request as RestRequest
from libs.responses import ApiResponse as BaseApiResponse
from configs.settings import BASE_DIR


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

class BaseApiHandler:
    api_view                                    = decorators.api_view
    ApiResponse: BaseApiResponse                = BaseApiResponse
    ApiPagination: ApiResponse.APIPagination    = ApiResponse.APIPagination

class BaseApiUsecase:
    _context: RestRequest

    errors: any
    meta_response: str = 'S1000'

    def __init__(self, context: RestRequest = None) -> None:
        self._context = context
