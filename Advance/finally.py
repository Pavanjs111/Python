print("Started learning python")
try:
    num=int(input("Enter the value for numerator"))
    den=int(input("Enter the value for denominator"))
    res=num//den
    print(res)
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("do it now")