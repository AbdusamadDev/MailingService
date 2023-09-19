import datetime
import pytz


def get_local_time():
    current_utc_time = datetime.datetime.now(pytz.utc)
    local_time = current_utc_time.astimezone().replace(tzinfo=None)
    return local_time
