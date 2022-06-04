from http.client import BAD_REQUEST
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.app_config import app_config
from utils.api_response import ApiResponse
from validators.posts.mail_hook import is_post_mail_hook
from django.core.mail import send_mail

class MailerView:

    @api_view(['POST'])
    @is_post_mail_hook
    def main(request: Request) -> Response:
        if request.error_data:
            return ApiResponse(data=request.error_data, status=BAD_REQUEST)

        data = request.valid_data

        send_mail(
            subject='Someone contacted you',
            message='',
            html_message=f"<h4>From: {data.get('sender_name')} &lt;{data.get('sender_email')}&gt;</h4><b>Message:</b><p>{data.get('message')}</p>",
            from_email=app_config.get('email_host_user'),
            recipient_list=app_config.get('contact_receipent')
        )

        send_mail(
            subject='Thank you for contacting :)',
            message='',
            html_message=f"<p>Dear {data.get('sender_name')},</p><p>Your message has been forwarded to <b>Aziz Ruri Suparman</b>!</p><br><p>From: <b>{data.get('sender_name')} &lt;{data.get('sender_email')}&gt;</b><br>Message:<br><em>{data.get('message')}</em></p><br><p>Thank you! :)</p>",
            from_email=app_config.get('email_host_user'),
            recipient_list=[data.get('sender_email')]
        )

        return ApiResponse(data)