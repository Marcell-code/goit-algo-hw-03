import datetime


def get_days_from_today(date):

    today_date = datetime.date.today()
    while True:
        try:
           your_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
           break
        except ValueError:
           return None
        
    date_delta =  today_date - your_date

    return int(date_delta.days)



print(get_days_from_today("2027-09-20"))
