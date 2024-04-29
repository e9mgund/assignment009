import datetime

def get_month(dt):
    return dt.strftime('%B')



print(get_month(datetime.datetime.now()))