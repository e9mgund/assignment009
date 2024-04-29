import datetime as dt
from pytz import timezone

def timezoneConverter(timezones):
    try:
        for i in timezones:
            print(i,dt.datetime.time(dt.datetime.now(timezone(i))))
    except Exception as e:
        print("Not a valid timezone.")



timezoneConverter(['US/Arizona',"Asia/Kolkata"])