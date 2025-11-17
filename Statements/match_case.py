# Alternative to using many elif statements

def weekdays(day):
    match day:
        case 1:
            return "Its Sunday!"
        case 2:
            return "Its Monday!"
        case 3:
            return "Its Tuesday!"
        case 4:
            return "Its Wednesday!"
        case 5:
            return "Its Thursday!"
        case 6:
            return "Its Friday!"
        case 7:
            return "Sunday!"


x = weekdays(1)
print(x)
