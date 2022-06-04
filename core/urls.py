from django.urls import include, re_path

urlpatterns = [
    re_path(r"^hook/", include('hooks.urls', namespace='webhooks'))
]

handler404 = 'utils.error_handlers.page_not_found'
handler500 = 'utils.error_handlers.server_error'