from typing import Optional
from django.db.models import QuerySet
from models.www_guest_subscribe.models import WWWGuestSubscribe
from utils.base.repository import BaseRepository


class WWWGuestSubscribeRepository(BaseRepository):
    main_model = WWWGuestSubscribe

    queryset: QuerySet[WWWGuestSubscribe]

    def __init__(self, qs: Optional[QuerySet[WWWGuestSubscribe]] = None) -> None:
        super().__init__(qs)

    def with_filter(self, *args, **kwargs) -> "WWWGuestSubscribeRepository":
        return super().with_filter(*args, **kwargs)