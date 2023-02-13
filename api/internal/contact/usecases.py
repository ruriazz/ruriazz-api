import pytz
from datetime import datetime
from django.core.mail import EmailMessage
from libs.extensions import BaseApiUsecase
from configs.settings import EMAIL_HOST_USER, EMAIL_NOTIFICATION_RECEIPIENT


class ContactApiUsecase(BaseApiUsecase):
    def submit_contact(self) -> bool:
        with open('views/templates/email/greeting_sender.html', 'r') as f:
            sender_name = str(self._context.data['senderName'].split(' ')[0]).title()
            content = str(f.read()).format(sender_name = sender_name)
            f.close()

        message = EmailMessage(subject='You just contacted ruriazz', body=content,  from_email=EMAIL_HOST_USER, to=[self._context.data['senderEmail']], reply_to=[EMAIL_NOTIFICATION_RECEIPIENT])
        message.content_subtype = 'html'
        sent = bool(message.send())
        if not sent:
            self.meta_response = 'E7012'
            self.errors = 'Failed to send e-mail'
            return

        with open('views/templates/email/forward_message.html', 'r') as f:
            content = str(f.read()).format(
                sender_name = str(self._context.data['senderName'].title()),
                sender_email = self._context.data['senderEmail'],
                message = self._context.data['message'],
                time = (datetime.now(tz=pytz.timezone('Asia/Jakarta'))).strftime('%d-%m-%Y %H:%M:%S %Z')
            )
            f.close()

        notification = EmailMessage(subject='New Message for You', body=content, from_email=EMAIL_HOST_USER, to=[EMAIL_NOTIFICATION_RECEIPIENT], reply_to=[self._context.data['senderEmail']])
        notification.content_subtype = 'html'
        notification.send()

        return sent