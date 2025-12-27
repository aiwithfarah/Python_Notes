def safe_division(a, b):

    result = 0
    try:
        #Risky code goes here
        result = a/b
        return result
    except ZeroDivisionError:
        err_msg = "Cannot divide by Zero"
    except TypeError:
        err_msg = "Types of a and b do not Match"
    except Exception as e:
        #to catch unexpected errors
        err_msg = f'Unexpected Error: {e}'

    print(err_msg.strip())
        
    with open('error_log.txt', 'a') as file:
        file.write(err_msg)
    return None

print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "hello"))
