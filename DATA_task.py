import datetime

today_date = datetime.date.today()
while True:
    try:
       date_str = input("Введіть дату у форматі рік.місяць.день: ")
       your_date = datetime.datetime.strptime(date_str, "%Y.%m.%d").date()
       break
    except ValueError:
        print("Невірний формат вводу! Спробуйте ще раз.")
        
def get_days_fromm_today(your_date):

    
    date_delta =  today_date - your_date

    print(f"Кількість днів від сьогодні до {your_date}: {date_delta.days} днів")


get_days_fromm_today(your_date)