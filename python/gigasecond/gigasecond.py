import datetime
from datetime import timedelta

def add_gigasecond(birth_date):
    billion_seconds = datetime.timedelta(seconds = 10**9)
    return birth_date + billion_seconds
