
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by Zero")
except ValueError:
    print("Enter only numbers please")
except Exception:  # Here we catch all unseen exception
    print("Something went wrong!")
finally:  # this block always executes regardless of whether there is an exception or not
    print("Do some clean up here")
