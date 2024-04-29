import calendar

def get_no_of_days(dt):
    return calendar.monthrange(dt.year,dt.month)[1]
