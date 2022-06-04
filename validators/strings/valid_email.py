import re

REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def valid_email(value: str) -> re.Match:
    if not value:
        return None

    value = value.strip()

    return re.search(REGEX, value)