from enum import Enum
from typing import Optional


class WWWTopic(str, Enum):
    WebReleased = 'web-released'

    @staticmethod
    def from_str(value: str) -> Optional["WWWTopic"]:
        try:
            return WWWTopic(value)
        except ValueError:
            pass