# Your task is to write and test a function which takes two arguments (a year and a month)
# and returns the number of days for the given year-month pair (while only February is sensitive to the year value,
#  your function should be universal).

def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):

    if 1 <= month >= 12:
        return "Invalid Month Number"

    if month == 2:
        return 29 if is_leap_year(year) else 28

    if month in (4, 6, 9, 11):
        return 30

    return 31


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
