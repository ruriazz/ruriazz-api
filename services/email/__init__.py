from typing import List, Optional
from django.core.mail import send_mail
from django.conf import settings

from utils.base.service import BaseService


class _SMTP(BaseService):
    _from: str = settings.EMAIL_HOST_USER
    _recipients: List[str]
    _subject: str
    _body: str

    def __init__(self, recipients: List[str], subject: str, body: str) -> None:
        super().__init__()

        self._recipients = recipients
        self._subject = subject
        self._body = body


class PlainTextEmail(_SMTP):
    def send(self) -> Optional[Exception]:
        try:
            send_mail(
                subject=self._subject,
                from_email=self._from,
                recipient_list=self._recipients,
                message=self._body
            )
        except Exception as err:
            return err


class HTMLEmail(_SMTP):
    pass