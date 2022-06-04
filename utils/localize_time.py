import pytz
from datetime import datetime
from core.settings import TIME_ZONE
from utils.middleware.application import get_client_timezone

def localize_time(time: datetime = None) -> datetime:
    tz = get_client_timezone()

    if not time:
        return datetime.now(tz=pytz.timezone(tz))

    local_time = pytz.timezone(tz)
    try:
        return local_time.localize(time)
    except:
        return time.replace(tzinfo=pytz.utc).astimezone(local_time)