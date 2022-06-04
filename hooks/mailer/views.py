from http.client import BAD_REQUEST
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.app_config import app_config
from utils.api_response import ApiResponse
from validators.posts.mail_hook import is_post_mail_hook
from utils.sendinblue import SendInBlue as SIB

class MailerView:

    @api_view(['POST'])
    @is_post_mail_hook
    def main(request: Request) -> Response:
        if request.error_data:
            return ApiResponse(data=request.error_data, status=BAD_REQUEST)

        data = request.valid_data

        SIB.create_contact(email=data.get('sender_email'), name=data.get('sender_name'))
        SIB.send_email(
            subject='Thank you for contacting :)',
            html_message=f"<p>Dear {data.get('sender_name')},</p><p>Your message has been forwarded to <b>Aziz Ruri Suparman</b>!</p><br><p>From: <b>{data.get('sender_name')} &lt;{data.get('sender_email')}&gt;</b><br>Message:<br><em>{data.get('message')}</em></p><p>Thank you! :)</p>",
            from_email={
                "name": app_config.get('contact_name'),
                "email": app_config.get('email_host_user')
            },
            reply_to={
                "name": app_config.get('contact_name'),
                "email": app_config.get('contact_reply_to')
            },
            receipents={
                "name": data.get('sender_name'),
                "email": data.get('sender_email')
            }
        )

        SIB.send_email(
            subject='Someone contacted you!',
            html_message=f"<h4>From: {data.get('sender_name')} &lt;{data.get('sender_email')}&gt;</h4><b>Message:</b><p>{data.get('message')}</p>",
            from_email={
                "name": data.get('sender_name'),
                "email": app_config.get('email_host_user')
            },
            reply_to={
                "name": data.get('sender_name'),
                "email": data.get('sender_email')
            },
            receipents={
                "name": app_config.get('contact_name'),
                "email": app_config.get('contact_receipent')
            }
        )

        return ApiResponse(data)