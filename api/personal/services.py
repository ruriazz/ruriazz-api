from typing import Type
from django.conf import settings
from application import const
from services.email import PlainTextEmail
from utils.base.service import BaseService
from . import entities


class PersonalContact(BaseService):
    _data: entities.PostContactData

    def __init__(self, data: entities.PostContactData) -> None:
        super().__init__()

        self._data = data
        self._main()

    def _main(self) -> Type["PersonalContact"]:
        message = f"sender: {self._data.sender_email}\n\nmessage:\n{self._data.message}"
        if _ := PlainTextEmail(recipients=settings.EMAIL_CONTACT_RECIPIENTS, subject=f"{self._data.sender_name} menghubungi melalui contact page", body=message).send():
            return self.with_error(Exception("failed to send message"))

        if _ := PlainTextEmail(recipients=[self._data.sender_email], subject='Pesan telah diterima', body=const.CONTACT_GREETING).send():
            return self.with_error(Exception(f"failed send greeting to '{self._data.sender_email}'"))