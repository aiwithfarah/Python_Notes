import datetime

date = datetime.date(2025, 12, 13)
print(date)  # 2025-12-13

today = datetime.date.today()
print(today)  # 2025-11-23

time = datetime.time(16, 30, 53)
print(time)  # 16:30:53

current_time = datetime.datetime.now()
print(current_time)  # 2025-11-23 18:00:17.394130

current_time = current_time.strftime("%H : %M : %S %m-%d-%Y")
print(current_time)  # 18 : 03 : 41 11-23-2025
