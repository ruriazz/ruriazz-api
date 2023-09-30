from models._enums.www_topic import WWWTopic
from repositories.www_guest_subscribe import WWWGuestSubscribeRepository
from services.email import PlainTextEmail
from utils.base.service import BaseService
from application import const
from . import entities


class GuestSubscribe(BaseService):
    def __init__(self, data: entities.PostGuestSubscribeData) -> None:
        super().__init__()

        if not WWWTopic.from_str(data.topic):
            self.with_error(Exception(f"'{data.topic}' is invalid topic"))
            return

        repo = WWWGuestSubscribeRepository().with_filter(email=data.email)
        if repo.queryset.exists():
            if repo.find_one(topics__contains=data.topic):
                return self._send_greeting(data.email)

            if not repo.update(topics=repo.queryset.first().topics + [data.topic]):
                self.with_error(Exception("failed to subscribe this topic"))
                return

            return self._send_greeting(data.email)
        else:
            WWWGuestSubscribeRepository().create_one(email=data.email, topics=[data.topic])
            return self._send_greeting(data.email)

    def _send_greeting(self, recipient: str) -> None:
        PlainTextEmail(recipients=[recipient], subject='Thank you!', body=const.WWW_GUEST_SUBSCRIBE_GREETING).send()