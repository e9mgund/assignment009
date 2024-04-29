import datetime

from ...get_no_of_days import get_no_of_days


def display_days(data):
    data = list(map(int,data.split("/")))
    return get_no_of_days(datetime.datetime(data[0],data[1],data[2]))


print(display_days("2024/04/29"))