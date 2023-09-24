from datetime import datetime
import pytz
import time


def get_time(given_dt_str):
    local_timezone = pytz.timezone("Asia/Tashkent")
    given_dt = datetime.strptime(given_dt_str, "%Y-%m-%d %H:%M:%S")
    given_dt_localized = local_timezone.localize(given_dt)
    given_unix_timestamp = given_dt_localized.timestamp()
    current_unix_timestamp = time.time()
    difference_in_unix = given_unix_timestamp - current_unix_timestamp
    return -(-(difference_in_unix))
