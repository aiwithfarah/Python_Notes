# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month)
#  and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

def is_year_leap(year):

    return (year & 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):

    if not 1 <= month <= 12:
        return "Invalid month number."

    if month == 2:
        return 29 if is_year_leap() else 28

    if month in (4, 6, 9, 11):
        return 30

    return 31


def day_of_year(year, month, day):
    # Tuple representing days in a month. 0 is ignored
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        days_in_month[2] = 29

    # 3. Calculate the day of the year.
    # The 'day of year' is the sum of days in all PRECEDING months, plus the current 'day'.
    ordinal_day = 0

    # Sum up the days from January (m=1) up to the month BEFORE the input month.
    # If month is 3 (March), the loop runs for m=1 (Jan) and m=2 (Feb)
    for m in range(1, month):
        ordinal_day += days_in_month[m]

    # Add the day of the current month.
    ordinal_day += day

    if ordinal_day > 0 and day > days_in_month[month]:
        return "Invalid Day Input for thid month"

    return ordinal_day


print(day_of_year(2000, 12, 30))
