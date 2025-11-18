stocks = [('APP', 400), ('MSFT', 200), ('GOOG', 300)]

for item in stocks:
    print(item)

# ('APP', 400)
# ('MSFT', 200)
# ('GOOG', 300)

# OR
for stock, price in stocks:
    print(stock)

# APP
# MSFT
# GOOG

work_hours = [('Abby', 300), ('Far', 1000), ('Sal', 600)]


def hero_of_the_month(work_hours):

    current_max = 0
    empl = ''

    for name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            empl = name
    return (empl, current_max)


x = hero_of_the_month(work_hours)
print(x)  # ('Far', 1000)
