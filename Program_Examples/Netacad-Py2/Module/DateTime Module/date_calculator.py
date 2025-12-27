from datetime import date, datetime, timedelta

current_date = date.today()
print(current_date)

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
print(current_time)

seven_days_from_now = current_date + timedelta(days=7)
print(seven_days_from_now)
