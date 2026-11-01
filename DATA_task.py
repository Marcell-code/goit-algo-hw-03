import datetime

def get_days_fromm_today(date):

    today_date = datetime.date.today()
    while True:
        try:
           your_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
           break
        except ValueError:
           print("Невірний формат.")
    
    date_delta =  today_date - your_date

    return f"Кількість днів  {date_delta.days} "


get_days_fromm_today("2023-10-27")
